import socket

c = socket.socket()
c.connect(("localhost", 8000))
data = c.recv(1024).decode()
open("received", "w").write(data)