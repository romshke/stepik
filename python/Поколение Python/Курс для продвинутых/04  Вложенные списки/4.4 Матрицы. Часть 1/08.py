n, m = int(input()), int(input())
result = list()
subresult = list()

for i in range(n):
    for j in range(m):
        subresult.append(input())
    result.append(subresult.copy())
    subresult.clear()

for i in range(n):
    print(*result[i])