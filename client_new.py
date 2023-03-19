import socket
import threading

HOST = '127.0.0.1'
PORT = 11111


def read_sok():
    while True:
        data = s.recv(1024)
        print(data.decode('utf-8'))


server = HOST, PORT
alias = input('Input your name: ')

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('', 0))
    s.sendto((alias + ' Connect to server').encode('utf-8'), server)
    potok = threading.Thread(target=read_sok)
    potok.start()
    while True:
        mensahe = input()
        s.sendto(('['+alias+']'+mensahe).encode('utf-8'), server)
