def sq_sum(*args):
    return sum(_**2 for _ in args)
    # return sum(map(lambda _: _**2, args))

print(sq_sum())
print(sq_sum(2))
print(sq_sum(1.5, 2.5))
print(sq_sum(1, 2, 3))
print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))