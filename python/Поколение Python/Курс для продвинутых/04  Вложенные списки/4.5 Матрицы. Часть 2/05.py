n = int(input())
l = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    l[i] = list(map(int, input().split()))

for i in range(n):
    # print(l[i][i], l[n-i-1][i])
    l[i][i], l[n-i-1][i] = l[n-i-1][i], l[i][i]
       
for i in range(n):
    print(*l[i])