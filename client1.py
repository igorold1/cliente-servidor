import socket
import threading

apelido = input("Digite o seu nick no servidor: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'APE':
                client.send(apelido.encode('ascii'))
            else:
                print(message)
        except:
            print("Um erro aconteceu!")
            client.close()
            break

def write():
    while True:
        message = f'{apelido}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
