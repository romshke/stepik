l = list()

for i in range(int(input())):
    l.append(input())
k = int(input())

for s in l:
    if len(s) >= k: print(s[k - 1], end='')