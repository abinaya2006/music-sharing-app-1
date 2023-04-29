import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def acceptConnections():
    global SERVER,clients

    while True:
        client,addr = SERVER.accept()
        print(client.addr)
    

def setup():
    print("\n\n\t\t IP MESSENGER \n")

    global SERVER,IP_ADDRESS,PORT

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))

    SERVER.listen(100)

    print("\n\t\tServe is ready to accept connections\n")

    acceptConnections()

setup_target = Thread(target=setup)
setup_target.start()

