n, m = map(int, input().split())

for i in range(n):
    print(*[str(_).ljust(3) for _ in [_ for _ in range(1 + i * m, m + 1 + i * m)]] if i % 2 == 0 else [str(_).ljust(3) for _ in [_ for _ in range(1 + i * m, m + 1 + i * m)]][::-1])