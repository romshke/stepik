from sys import maxsize

n = int(input())
maximum = -maxsize

for i in range(n):
    l = list(map(int, input().split()))
    
    for j in range(i + 1):
        maximum = max(l[j], maximum)

print(maximum)
