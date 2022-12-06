n = int(input())

print(
    *list(list(range(1, _ + 2)) for _ in range(n)), sep='\n'
)