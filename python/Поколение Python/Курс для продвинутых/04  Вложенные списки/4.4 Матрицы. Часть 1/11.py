n = int(input())
result = 0

for i in range(n):
    l = list(map(int, input().split()))
    count = 0
    
    for j in l:
        if sum(l) / len(l) < j:
            count += 1
        
    print(count)