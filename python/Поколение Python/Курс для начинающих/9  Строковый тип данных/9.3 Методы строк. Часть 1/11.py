s = input()
count = 0

for i, j in zip(s, s.upper()):
    if i != j:
        count += 1
print(count)