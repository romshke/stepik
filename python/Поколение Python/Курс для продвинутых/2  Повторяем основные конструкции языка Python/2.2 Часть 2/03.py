l = list(map(int, input().split()))

for i in range(0, len(l), 2):
    try:
        l[i], l[i + 1] = l[i + 1], l[i]
    except:
        continue
print(*l)