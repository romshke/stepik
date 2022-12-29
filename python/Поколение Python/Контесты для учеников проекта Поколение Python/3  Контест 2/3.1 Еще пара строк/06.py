a, b = input(), input()

print(*set(map(lambda _: _ if a.count(_) != b.count(_) else '', b)), sep='')