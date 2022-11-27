n = int(input())
result = 0

for i in range(n):
    result += list(map(int, input().split()))[i]
    
print(result)