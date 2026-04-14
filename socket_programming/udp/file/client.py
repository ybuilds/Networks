import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.sendto("send file".encode(), ("localhost", 8000))
data, _ = c.recvfrom(1024)
open("received", "w").write(data.decode())