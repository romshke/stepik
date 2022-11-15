l = list()

for _ in range(int(input())):
    s = input()
    if l.count(s) != 0: continue
    else: l.append(s)

print(*l, sep='\n')