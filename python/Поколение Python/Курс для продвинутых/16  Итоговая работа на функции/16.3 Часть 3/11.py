ips = [input() for _ in range(int(input()))]

def ip_2_dec(ip):
    return sum(map(lambda index, value: value * 256**index, [_ for _ in range(len(list(map(int, ip.split('.')))) - 1, -1, -1)], map(int, ip.split('.'))))

print(*sorted(ips, key=ip_2_dec), sep='\n')