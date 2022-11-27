n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j > i:
            matrix[i][j] = j - i
            matrix[j][i] = j - i

    print(*matrix[i])