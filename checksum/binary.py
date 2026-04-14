def add(csum, val):
    csum += val
    while csum > 0xFF:
        csum = (csum & 0xFF) + (csum >> 8)
    return csum

def tobin(val):
    return format(int(val), "08b")

data = input("Enter space separated binary data: ").split(" ")
senderSum = 0
for d in data:
    senderSum = add(senderSum, int(d, 2))
senderChecksum = ~senderSum & 0xFF

print("Sender sum =", tobin(senderSum))
print("Sender checksum =", tobin(senderChecksum))

data = input("Enter space separated received binary data: ").split(" ")
receiverSum = 0
for d in data:
    receiverSum = add(receiverSum, int(d, 2))
receiverSum = add(receiverSum, senderChecksum)
receiverChecksum = ~receiverSum & 0xFF

print("Receiver sum =", tobin(receiverSum))
print("Receiver checksum =", tobin(receiverChecksum))

if receiverChecksum == 0:
    print("Data accepted")
else:
    print("Data not accepted")