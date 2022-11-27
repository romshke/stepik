n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n // 2 + 1):
    matrix[i][i:n - i] = [1 for _ in range(i, n - i)]
    matrix[n - i - 1][i:n - i] = [1 for _ in range(i, n - i)]

for i in range(n):
    print(*list(str(_).ljust(3) for _ in matrix[i]))