n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()