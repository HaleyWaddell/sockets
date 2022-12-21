import socket

if name== "main":
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.connect((ip, port))