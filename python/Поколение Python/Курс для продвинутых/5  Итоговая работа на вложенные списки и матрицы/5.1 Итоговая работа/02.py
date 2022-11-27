from sys import maxsize


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
maximum = -maxsize

for i in range(n):
    # print(matrix[i][n - i - 1:])
    for _ in matrix[i][n - i - 1:]:
        if _ > maximum:
            maximum = _
        
print(maximum)