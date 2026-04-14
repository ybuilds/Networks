def count_one(val):
    ones = 0
    for c in val:
        if c == '1':
            ones += 1
    return ones

def generate(val, ch):
    ones = count_one(val)
    if ch == 1:
        if ones%2 == 0:
            return val + "0"
        else:
            return val + "1"
    else:
        if ones % 2 == 0:
            return val + "1"
        else:
            return val + "0"

def verify(val, ch):
    ones = count_one(val)
    if ch == 1:
        return ones%2 == 0
    else:
        return ones%2 != 0

choice = int(input("1.Even 2.Odd; Choose parity: "))
data = input("Enter binary data: ")
sent = generate(data, choice)
print("Generated data =", sent)

data = input("Enter received binary data: ")
if verify(data, choice):
    print("Data accepted")
else:
    print("Data corrupted")