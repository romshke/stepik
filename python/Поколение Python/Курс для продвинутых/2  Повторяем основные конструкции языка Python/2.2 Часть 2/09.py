result = 0
count = 0

for _ in input():
    if _ == 'Р':
        count += 1
    if _ == 'О':
        result = max(result, count)
        count = 0
        
result = max(result, count)
print(result)