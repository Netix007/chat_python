import socket

HOST = '127.0.0.1'
PORT = 11111

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    clients = []
    print('Start Server')
    while True:
        data, address = s.recvfrom(1024)
        if address not in clients:
            clients.append(address)
            print('Connection: ' + address[0] + ':' + str(address[1]))
        for client in clients:
            if client == address:
                continue
            s.sendto(data, client)
