n, list = int(input()), []

for _ in range(n):
    list.append(int(input()))
        
print(sorted(list)[-1], sorted(list)[-2], sep='\n')