def bin32(ip):
    return ".".join(format(int(x), "08b") for x in ip.split("."))

def valid(ip):
    p = ip.split(".")
    return len(p) == 4 and all(x.isdigit() and 0 <= int(x) <= 255 for x in p)

def ip_class(first):
    if 1 <= first <= 126: return "A", "255.0.0.0"
    if 128 <= first <= 191: return "B", "255.255.0.0"
    if 192 <= first <= 223: return "C", "255.255.255.0"
    return "Invalid", "-"

def borrowed(prefix, cls):
    d = {"A":8, "B":16, "C":24}
    return prefix - d[cls]

def net_host(ip):
    p = ip.split(".")
    c = ip_class(int(p[0]))[0]
    if c == "A": return ".".join([p[0],"0","0","0"]), ".".join(["0",p[1],p[2],p[3]])
    if c == "B": return ".".join([p[0],p[1],"0","0"]), ".".join(["0","0",p[2],p[3]])
    if c == "C": return ".".join([p[0],p[1],p[2],"0"]), ".".join(["0","0","0",p[3]])
    return "-", "-"

# ---------- PART 1 ----------
ip = "140.65.0.0"
prefix = 26

print("PART 1")

cls, dmask = ip_class(int(ip.split(".")[0]))
print("Class :", cls)
print("Default Mask :", dmask)

mask = [0,0,0,0]
for i in range(prefix):
    mask[i//8] += 1 << (7-i%8)
cmask = ".".join(map(str, mask))
print("Custom Mask :", cmask)

b = borrowed(prefix, cls)
print("Bits Borrowed :", b)
print("Total Subnets :", 2**b)

hosts = 2**(32-prefix)
print("Total Host Addresses :", hosts)
print("Usable Addresses :", hosts-2)

step = 256 - mask[3]
print("10th Subnet :", f"140.65.{(9*step)//256}.{(9*step)%256}")
print("20th Subnet :", f"140.65.{(19*step)//256}.{(19*step)%256}")

print("Valid IP :", "Yes" if valid(ip) else "No")

nid, hid = net_host(ip)
print("Net ID :", nid)
print("Host ID :", hid)

# ---------- PART 2 ----------
print("\nPART 2")

ip2 = "192.168.10.0"
print("32 bit Binary :", bin32(ip2))

cls, dmask = ip_class(int(ip2.split(".")[0]))
print("Class :", cls)
print("Default Mask :", dmask)

# VLSM for 64,32,64,32 addresses
req = [64,32,64,32]
base = 0

for i,n in enumerate(req,1):
    h = 0
    while 2**h < n:
        h += 1
    pre = 32-h

    m = [0,0,0,0]
    for j in range(pre):
        m[j//8] += 1 << (7-j%8)

    size = 2**h
    print(f"\nSubnet {i}")
    print("Network :", f"192.168.10.{base}")
    print("Mask :", ".".join(map(str,m)), f"/{pre}")
    print("Total Hosts :", size)
    print("Usable :", size-2)
    print("Bits Borrowed :", pre-24)

    base += size

print("\nValid IP :", "Yes" if valid(ip2) else "No")

nid, hid = net_host(ip2)
print("Net ID :", nid)
print("Host ID :", hid)