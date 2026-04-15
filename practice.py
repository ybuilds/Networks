def crc(d, k):
    n = len(k) - 1
    msg = list(d + "0"*n)
    for i in range(len(d)):
        if msg[i] == "1":
            for j in range(len(k)):
                msg[i+j] = str(int(msg[i+j] != k[j]))
    return "".join(msg[-n:])

data = input("Data: ")
key = input("Key: ")
rem = crc(data, key)
code = data + rem
print("CRC:", code)

r = input("Received: ")
if crc(r[:-len(rem)], key) == r[-len(rem):]:
    print("True")
else:
    print("False")