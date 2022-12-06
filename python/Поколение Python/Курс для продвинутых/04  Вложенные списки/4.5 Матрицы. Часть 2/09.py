n = int(input())
l = [[0 for i in range(n)] for j in range(n)]
s = set()
flag = True
rows = [0 for _ in range(n)]
columns = [0 for _ in range(n)]
diagonals = [0, 0]

for i in range(n):
    l[i] = list(map(int, input().split()))
    
    rows[i] = sum(l[i])
    
    for _ in l[i]:
        s.add(_)
        
    if 0 in s:
        flag = False
        break

if rows.count(rows[0]) != n:
    flag = False
    
if len(s) != n**2:
    flag = False
    
if flag:
    for i in range(n):
        diagonals[0] += l[i][i]
        diagonals[1] += l[-i][-i]
        columns[i] = sum(l[j][i] for j in range(n))
    
    if set(rows) == set(columns) == set(diagonals):
        print('YES')
    else:
        print('NO')
else:
    print('NO')