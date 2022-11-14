x = list()
for _ in range(int(input())):
    x.append(int(input()))

print(*x, sep='\n')
print()
for _ in x: print(_**2 + _*2 + 1)