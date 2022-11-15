n, l = int(input()), list()

for _ in range(n): l.append(int(input()))
del l[1::2]

print(l)