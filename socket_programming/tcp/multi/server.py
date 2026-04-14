import socket, threading

clients = []

def handle(cl):
    while True:
        try:
            msg = cl.recv(1024)
            for client in clients:
                if client != cl:
                    client.send(msg)
        except OSError:
            break
    clients.remove(cl)

s = socket.socket()
s.bind(("localhost", 8000))
s.listen()

while True:
    c, a = s.accept()
    clients.append(c)
    threading.Thread(target=handle, args=(c,)).start()