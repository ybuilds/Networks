import socket

s = socket.socket()
s.bind(("localhost", 8000))
s.listen()
c, a = s.accept()

while True:
    msg = c.recv(1024).decode()
    print("Client:", msg)
    reply = input("Server: ")
    c.send(reply.encode())