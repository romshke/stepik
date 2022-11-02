n = int(input())
total = 0

for _ in range(1, n + 1):
    if n%_ == 0: total += _
print(total)