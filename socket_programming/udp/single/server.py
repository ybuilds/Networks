import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 8000))

while True:
    msg, a = s.recvfrom(1024)
    print("Client:", msg.decode())
    reply = input("Server: ")
    s.sendto(reply.encode(), a)