n, l = int(input()), list()

for _ in range(n):
    x = int(input())
    if _ == 0: l.append(x)
    elif _ < n - 1: 
        l[_ - 1] += x
        l.append(x)
    else: l[_ - 1] += x
print(l)