n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
flag = True

pattern = [_ for _ in range(1, n + 1)]

for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(matrix[j][i])
    
    for _ in pattern:
        if not _ in matrix[i] or not _ in tmp:
            flag = False
            break
    
    if not flag:
        break
    
print('YES' if flag else 'NO')