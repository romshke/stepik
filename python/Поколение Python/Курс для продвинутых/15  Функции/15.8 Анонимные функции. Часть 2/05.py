func = lambda _: True if _ % 19 == 0 or _ % 13 == 0 else False

print(func(19))
print(func(13))
print(func(20))
print(func(15))
print(func(247))