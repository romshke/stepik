n = int(input())
l = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    l[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        print(l[n - j - 1][i], end=' ')
    print()