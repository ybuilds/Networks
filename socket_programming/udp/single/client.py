import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Client: ")
    c.sendto(msg.encode(), ("localhost", 8000))
    reply, _ = c.recvfrom(1024)
    print("Server:", reply.decode())