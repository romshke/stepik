n, m = map(int, input().split())

for i in range(n):
    print(*[_ for _ in range(i % m + 1, m + 1)] + [_ for _ in range(1, i % m + 1)])