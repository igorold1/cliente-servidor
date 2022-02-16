import threading
import socket

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
apelidos = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            apelido = apelidos[index]
            broadcast(f'{apelido} saiu da conversa!'.encode('ascii'))
            apelidos.remove(apelido)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Conectado a {str(address)}")

        client.send('APE'.encode('ascii'))
        apelido = client.recv(1024).decode('ascii')
        apelidos.append(apelido)
        clients.append(client)

        print(f'O apelido do usuario é {apelido}!')
        broadcast(f'{apelido} se juntou ao chat!'.encode('ascii'))
        client.send('Conectado ao servidor!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
receive()

