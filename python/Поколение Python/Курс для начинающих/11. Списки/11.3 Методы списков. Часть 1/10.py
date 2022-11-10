n = int(input())
print(
    list(
        _ for _ in range(1, n + 1) if n % _ == 0
    )
)