from functools import reduce

k = int(input())

print(*reduce(lambda x, y: x + y, [[x for y in range(x)] for x in range(1, k + 1)], [])[:k])