def mean(*args):
    numbers = list(_ for _ in args if type(_) == int or type(_) == float)
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0.0


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
