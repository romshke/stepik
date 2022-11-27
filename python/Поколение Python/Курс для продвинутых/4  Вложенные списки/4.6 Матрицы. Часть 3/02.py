n = int(input())
l = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    l[i][:n - i - 1] = [0 for _ in range(n - i - 1)]
    l[i][n - i - 1] = 1
    l[i][n - i:] = [2 for _ in range(i)]
    print(*l[i])