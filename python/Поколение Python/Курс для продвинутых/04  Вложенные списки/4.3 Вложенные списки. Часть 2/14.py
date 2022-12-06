l = input().split()
result = [[]]

for i in range(len(l)):
    for j in range(len(l) - i):
        # print(l[j:j+i+1])
        result.append(l[j:j+i+1])

print(result)