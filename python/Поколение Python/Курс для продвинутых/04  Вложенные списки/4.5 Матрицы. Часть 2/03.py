n, m = int(input()), int(input())
l = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    l[i] = list(map(int, input().split()))

rows = list(map(int, input().split()))

for i in range(n):
    l[i][rows[0]], l[i][rows[1]] = l[i][rows[1]], l[i][rows[0]]

for i in range(n):
    print(*l[i])