n = int(input())
l = [[0 for i in range(n)] for j in range(n)]
flag = True

for i in range(n):
    l[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if l[i][j] != l[j][i]:
            flag = False
            break
    if not flag:
        break

print('YES' if flag else 'NO')