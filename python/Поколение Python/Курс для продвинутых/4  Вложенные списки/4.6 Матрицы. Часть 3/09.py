n, m = map(int, input().split())
matrix = [[(i * m) + _ + 1 for _ in range(m)] for i in range(n)]

number = 0

for k in range(n + m - 1):
    for i in range(n):
        j = k - i
        if 0 <= i < n and 0 <= j < m:
            number += 1
            matrix[i][j] = number
        
for i in range(n):
    print(*list(str(_).ljust(3) for _ in matrix[i]))