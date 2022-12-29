numbers = [*range(1, int(input()) + 1)]

for _ in range(1, len(numbers)):
    numbers.remove(int(input()))

print(*numbers)