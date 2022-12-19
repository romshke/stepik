from functools import reduce


def product_of_odds(data):
    return reduce(lambda x, y: x * y, filter(lambda _: _ % 2 == 1, data), 1)