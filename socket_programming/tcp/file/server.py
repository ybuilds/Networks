import socket

s = socket.socket()
s.bind(("localhost", 8000))
s.listen()
c, _ = s.accept()
data = open("sent", "r").read()
c.send(data.encode())