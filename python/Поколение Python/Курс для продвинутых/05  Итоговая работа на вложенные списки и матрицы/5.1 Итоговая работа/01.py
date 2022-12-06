symbols = input().split()
n = int(input())
result = [[] for _ in range(n)]

for i in range(0, len(symbols), n):
    for j in range(n):
        try:
            result[j].append(symbols[j + i])
        except:
            continue
        
print(result)