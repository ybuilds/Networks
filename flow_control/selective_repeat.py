def sender(packet):
    print(f"Sending packet {packet}")

def receiver(packet, state):
    if state == 3:
        print(f"Packet {packet} lost in transmission")
        return False
    print(f"Packet {packet} received")

    if state == 2:
        print(f"Packet {packet} ACK lost")
        return False
    print(f"Packet {packet} ACK received")

    return True

n = int(input("Enter number of packets: "))
w = int(input("Enter window size: "))
action = {i:int(input(f"Action for packet {i}: 1.OK 2.ACK LOST 3.PACKET LOSS: ")) for i in range(1, n+1)}

ack = set()
base = 1

while base <= n:
    win = [p for p in range(base, min(base+w, n+1)) if p not in ack]
    fail = []

    for p in win:
        sender(p)

    for p in win:
        if receiver(p, action[p]):
            ack.add(p)
        else:
            fail.append(p)

    for p in fail:
        print(f"Timeout. Retransmitting {p}")
        sender(p)
        receiver(p, 1)
        ack.add(p)

    while base in ack:
        base += 1