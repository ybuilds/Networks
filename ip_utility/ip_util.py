cls = {"A": 8, "B": 16, "C": 24}

def to_binary(ip):
    return ".".join(format(int(x), "08b") for x in ip.split("."))

def ip_class_subnet(ip):
    first = int(ip.split(".")[0])
    if 0 <= first <= 127:   return "A", "255.0.0.0"
    if 128 <= first <= 191: return "B", "255.255.0.0"
    if 192 <= first <= 223: return "C", "255.255.255.0"
    if 224 <= first <= 239: return "D", "RES"
    if 240 <= first <= 255: return "E", "RES"
    return None

def net_host(ip):
    octets = ip.split(".")
    c = ip_class_subnet(ip)[0]
    if c == "A":  return octets[0] + ".0.0.0", "0." + octets[1] + "." + octets[2] + "." + octets[3]
    if c == "B":  return octets[0] + "." + octets[1] + ".0.0", "0.0" + "." + octets[2] + "." + octets[3]
    if c == "C":  return octets[0] + "." + octets[1] + "." + octets[2] + ".0", "0.0.0." + octets[3]
    if c == "D" or c == "E": return "RES", "RES"
    return None

def custom_subnet(p):
    mask = [0, 0, 0, 0]
    for i in range(p):
        mask[i//8] += 1 << (7 - i%8)
    return ".".join(map(str, mask))

def borrowed_total_subnets(ip, p):
    c, _ = ip_class_subnet(ip)
    if c not in cls:
        return "NA", "NA"
    return p - cls[c], 2 ** (p - cls[c])

def host_usable_addresses(p):
    return 2 ** (32-p), 2 ** (32-p) - 2

def ip_to_num(ip):
    octets = [int(x) for x in ip.split(".")]
    return (octets[0] * 256**3) + (octets[1] * 256**2) + (octets[2] * 256**1) + (octets[3] * 256**0)

def num_to_ip(num):
    a = num // 256**3
    b = (num // 256**2) % 256
    c = (num // 256**1) % 256
    d = (num // 256**0) % 256
    return str(a) + "." + str(b) + "." + str(c) + "." + str(d)

def get_nth_ip(ip, n):
    return num_to_ip(ip_to_num(ip) + n-1)

def get_subnet_adrs(ip, p, n):
    size = 2 ** (32-p)
    return num_to_ip(ip_to_num(ip) + (n-1) * size)

def vlsm(ip, req):
    cur = ip_to_num(ip)

    for i, r in enumerate(req):
        s = 1
        while s < r:
            s *= 2

        first = num_to_ip(cur)
        last = num_to_ip(cur + s - 1)

        print("Subnet", i+1, ". First and Last IP:", first, "&", last)

        cur += s

ip_adrs = input("Enter IP: ")
prefix = int(input("Enter Prefix (0 if none): "))
if prefix == 0:
    prefix = cls.get(ip_class_subnet(ip_adrs)[0])
print("Binary IP:", to_binary(ip_adrs))
print("Class and Default subnet:", ip_class_subnet(ip_adrs))
print("Net and Host ID:", net_host(ip_adrs))
print("Custom subnet:", custom_subnet(prefix))
print("Borrowed bits and Total subnets:", borrowed_total_subnets(ip_adrs, prefix))
print("Total host addresses and usable addresses:", host_usable_addresses(prefix))
print("IP of 10th and 20th subnet:", get_subnet_adrs(ip_adrs, prefix, 10), "&", get_subnet_adrs(ip_adrs, prefix, 20))
choice = int(input("Need subnets? 1.Yes 2.No: "))
if choice == 1:
    n = int(input("Enter number of subnets: "))
    require = [int(input(f"Enter addresses needed in subnet {i+1}: ")) for i in range(n)]
    vlsm(ip_adrs, require)