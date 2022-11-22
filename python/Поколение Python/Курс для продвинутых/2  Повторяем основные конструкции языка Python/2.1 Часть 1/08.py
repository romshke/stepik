s = input()
result = list()

if len(s) - (3 * (len(s) // 3)) != 0:
    rb = len(s) - (3 * (len(s) // 3))
else:
    rb = 3
lb = 0

while rb < len(s) + 3:
    result.append(s[lb:rb])
    lb = rb
    rb += 3

print(*result, sep=',')