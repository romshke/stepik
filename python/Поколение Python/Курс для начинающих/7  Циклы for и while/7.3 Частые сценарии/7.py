from math import log

n = int(input())
total = 0

for _ in range(n):
    total += 1 / (_ + 1)
print(total - log(n))
