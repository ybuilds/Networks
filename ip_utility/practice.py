cls = {"A":8, "B":16, "C":24}

def class_subnet(ip):
    first = int(ip[0])
    if 0 <= first <= 127:   return "A", "255.0.0.0"
    if 128 <= first <= 191: return "B", "255.255.0.0"
    if 192 <= first <= 223: return "C", "255.255.255.0"
    if 224 <= first <= 239: return "D", "NA"
    if 240 <= first <= 255: return "E", "NA"
    return None

def net_host_id(ip):
    ip_cls = class_subnet(ip)[0]
    if ip_cls == "A": return ip[0] + ".0.0.0", "0." + ip[1] + "." + ip[2] + "." + ip[3]
    if ip_cls == "B": return ip[0] + "." + ip[1] + ".0.0", "0.0." + ip[2] + "." + ip[3]
    if ip_cls == "C": return ip[0] + "." + ip[1] + "." + ip[2] + ".0", "0.0.0." + ip[3]
    if ip_cls == "D" or ip_cls == "E": return "NA", "NA"
    return None

def ip_to_num(ip):
    return (int(ip[0]) * 256**3) + (int(ip[1]) * 256**2) + (int(ip[2]) * 256**1) + (int(ip[3]) * 256**0)

def num_to_ip(num):
    a = num // 256**3
    b = (num // 256**2) % 256
    c = (num // 256 ** 1) % 256
    d = (num // 256 ** 0) % 256
    return f"{a}.{b}.{c}.{d}"

def nth_ip(ip, n):
    return num_to_ip(ip_to_num(ip) + n - 1)

def nth_subnet_ip(ip, n):
    return num_to_ip(ip_to_num(ip) + (n-1) * host)

def vlsm(ip, req):
    cur = ip_to_num(ip)

    for i, r in enumerate(req):
        s = 1
        while s-2 < r:
            s *= 2

        first = num_to_ip(cur)
        last = num_to_ip(cur + s - 1)

        print(f"First and last IP of subnet {i+1}: {first} & {last}")

        cur += s

ip_adrs = input("Enter IP in dotted decimal format: ").split(".")
ip_class, def_subnet = class_subnet(ip_adrs)
net_id, host_id = net_host_id(ip_adrs)

prefix = int(input("Enter prefix (0 if none): "))
if prefix == 0:
    prefix = cls[ip_class]

host = 2 ** (32 - prefix)
usable = host - 2
borrowed = prefix - cls[ip_class]
subnets = 2 ** borrowed

require = [64, 32, 64, 32]
vlsm(ip_adrs, require)