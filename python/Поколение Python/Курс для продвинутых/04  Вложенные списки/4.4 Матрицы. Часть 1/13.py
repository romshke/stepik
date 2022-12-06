from sys import maxsize

n = int(input())
maximum = -maxsize

for i in range(n):
    l = list(map(int, input().split()))

    if n // 2 > i:
        # print(l[:i + 1] + l[-(i + 1):])
        for j in l[:i + 1] + l[-(i + 1):]:
            maximum = max(j, maximum)
    else:
        # print(l[:n - i] + l[-(n - i):])
        for j in l[:n - i] + l[-(n - i):]:
            maximum = max(j, maximum)

print(maximum)