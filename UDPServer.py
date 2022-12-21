import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 12345))

#finite loop for sending/receiving data
while True:
    data,addr=sock.recvfrom(4096)
    print(str(data))
    message=bytes("Hello this is the UDP Server").encode('utf-8')
    sock.sendto(message,addr)