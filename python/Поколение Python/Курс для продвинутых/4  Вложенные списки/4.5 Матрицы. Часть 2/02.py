from sys import maxsize


n, m = int(input()), int(input())
l = [[0 for i in range(m)] for j in range(n)]
maximum = -maxsize
index = [0, 0]

for i in range(n):
    l[i] = list(map(int, input().split()))
    for j in range(m):
        if maximum < l[i][j]:
            maximum = l[i][j]
            index = i, j

print(*index)