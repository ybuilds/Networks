seq = 0

def sender(packet):
    print(f"Packet {packet} sent [SEQ: {seq}]")

def receiver(packet, state):
    if state == 3:
        print(f"Packet {packet} lost in transmission")
        return False
    print(f"Packet {packet} received [SEQ: {seq}]")

    if state == 2:
        print(f"Packet {packet} ACK lost")
        return False
    print(f"Packet {packet} ACK received [SEQ: {seq}]")

    return True

n = int(input("Enter number of packets: "))
action = {i: int(input(f"Action for packet {i}: 1.OK 2.ACK LOST 3.PACKET LOST: ")) for i in range(1, n+1)}

for p in range(1, n+1):
    sender(p)
    if not receiver(p, action[p]):
        print(f"Timeout. Retransmitting packet {p}")
        sender(p)
        receiver(p, 1)

    seq = 1 - seq