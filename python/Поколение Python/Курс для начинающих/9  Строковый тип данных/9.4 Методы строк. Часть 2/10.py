n, count = input(), 0

for _ in range(int(n)):
    if input().count('11') >= 3: count += 1
print(count)