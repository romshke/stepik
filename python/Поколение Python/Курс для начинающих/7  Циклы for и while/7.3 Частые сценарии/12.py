n, total = int(input()), 0

for _ in range(1, n + 1):
    if _%2 != 0: total += _
    else: total -= _
print(total)