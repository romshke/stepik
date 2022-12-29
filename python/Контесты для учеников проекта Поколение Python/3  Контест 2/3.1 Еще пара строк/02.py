numbers = []
zeros = []

for _ in input().split():
    numbers.append(_) if _ != '0' else zeros.append(_)

print(*numbers, *zeros)