def add(csum, val):
    csum += val
    while csum > 0xFFFF:
        csum = (csum & 0xFFFF) + (csum >> 16)
    return csum

data = input("Enter space separated hexadecimal data: ").split(" ")
senderSum = 0
for d in data:
    senderSum = add(senderSum, int(d, 16))
senderChecksum = ~senderSum & 0xFFFF

print("Sender sum =", hex(senderSum))
print("Sender checksum =", hex(senderChecksum))

data = input("Enter space separated received hexadecimal data: ").split(" ")
receiverSum = 0
for d in data:
    receiverSum = add(receiverSum, int(d, 16))
receiverSum = add(receiverSum, senderChecksum)
receiverChecksum = ~receiverSum & 0xFFFF

print("Receiver sum =", hex(receiverSum))
print("Receiver checksum =", hex(receiverChecksum))

if receiverChecksum == 0:
    print("Data accepted")
else:
    print("Data not accepted")