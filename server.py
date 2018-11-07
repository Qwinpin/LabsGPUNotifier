import socket

HOST = '192.168.0.245'
PORT = 5005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        connect, addr = s.accept()

        with connect:
            while True:
                data = connect.recv(4096)
                if not data:
                    break
                print(data)
