import socket

c = socket.socket()
c.connect(("localhost", 8000))

while True:
    msg = input("Client: ")
    c.send(msg.encode())
    reply = c.recv(1024).decode()
    print("Server:", reply)