import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 8000))
addresses = []

while True:
    msg, addr = s.recvfrom(1024)
    if addr not in addresses:
        addresses.append(addr)
    for a in addresses:
        if a != addr:
            s.sendto(msg, a)