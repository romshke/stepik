n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    matrix[i] = [i + _ + 1 + _ * (n - 1) for _ in range(m)]
    print(*list(str(_).ljust(3) for _ in matrix[i]))