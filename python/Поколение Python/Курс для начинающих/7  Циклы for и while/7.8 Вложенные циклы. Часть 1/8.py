n = int(input())

for i in range(n):
    if i < ((n // 2) + 1):
        for j in range(i + 1): print("*", end='')
    else:
        for j in range(n - i): print("*", end='')
    print()