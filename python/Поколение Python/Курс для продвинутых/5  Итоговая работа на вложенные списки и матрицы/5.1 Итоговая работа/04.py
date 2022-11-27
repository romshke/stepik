n = int(input())
matrix = [['.' for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = '*'
            matrix[i][-j - 1] = '*'
        if i == n // 2 or j == n // 2:
            matrix[i][j] = '*'
            
    print(*matrix[i])