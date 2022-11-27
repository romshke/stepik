n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
flag = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
            flag = False
            break
    if not flag:
        break

print('YES' if flag else 'NO')