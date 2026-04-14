import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 8000))
_, a = s.recvfrom(1024)
data = open("sent", "r").read()
s.sendto(data.encode(), a)