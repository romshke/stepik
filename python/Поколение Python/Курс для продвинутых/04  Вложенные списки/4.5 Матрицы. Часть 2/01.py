n, m = int(input()), int(input())
mult = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j

for i in range(n):
    for j in range(m):
        print(str(mult[i][j]).ljust(3), end='')
    print()