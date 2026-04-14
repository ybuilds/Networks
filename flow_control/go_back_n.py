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
action = {i: int(input(f"Action for packet {i}: 1.OK 2.ACK LOST 3.PACKET LOST: ")) for i in range(1, n+1)}

base = 1
while base <= n:
    fail = 0
    win = list(range(base, min(base+w, n+1)))

    for p in win:
        sender(p)

    for p in range(base, min(base+w, n+1)):
        if not receiver(p, action[p]):
            fail = p
            action[p] = 1
            break

    if fail:
        print(f"Retransmitting from packet {fail}")
        base = fail
    else:
        base += w