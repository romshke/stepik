cities = set()
for _ in range(int(input())):
    cities.add(input())
    
print('REPEAT' if input() in cities else 'OK')