from random import randint

result = set()

while len(result) != 7:
    result.add(randint(1, 49))

print(*sorted(result))