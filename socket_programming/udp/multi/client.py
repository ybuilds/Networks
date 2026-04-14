import socket, threading

def send():
    while True:
        c.sendto(input().encode(), ("localhost", 8000))

def receive():
    while True:
        msg, _ = c.recvfrom(1024)
        print("Friend:", msg.decode(), flush=True)

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
t1 = threading.Thread(target=send)
t2 = threading.Thread(target=receive)

t1.start()
t2.start()

t1.join()
t2.join()