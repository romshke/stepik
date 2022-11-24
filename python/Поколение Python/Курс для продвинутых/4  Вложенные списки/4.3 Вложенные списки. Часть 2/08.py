n = int(input())

print(
    *list(list(range(1, n + 1)) for _ in range(n)), sep='\n'
)