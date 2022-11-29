s = set()

for i in range(int(input())):
    for j in input().lower():
        s.add(j)

print(len(s))