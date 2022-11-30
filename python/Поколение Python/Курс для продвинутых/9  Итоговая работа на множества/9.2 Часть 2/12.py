result = set()

for i in range(int(input())):
    tmp = set()
    
    for j in range(int(input())):
        tmp.add(input())
    
    if i == 0:
        result = tmp
    else:
        result = result & tmp
    
print(*sorted(result), sep='\n')