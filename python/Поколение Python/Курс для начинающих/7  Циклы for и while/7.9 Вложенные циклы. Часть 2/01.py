n = int(input())
tmp = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        tmp += 1 
        print(tmp, end=' ')
    print()
