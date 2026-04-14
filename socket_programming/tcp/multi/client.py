import socket, threading

def send():
    while True:
        c.send(input().encode())

def receive():
    while True:
        print("Friend:", c.recv(1024).decode())

c = socket.socket()
c.connect(("localhost", 8000))
threading.Thread(target=send).start()
threading.Thread(target=receive).start()