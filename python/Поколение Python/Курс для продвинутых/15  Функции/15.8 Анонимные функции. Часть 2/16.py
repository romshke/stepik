from functools import reduce


def evaluate(coefficients, x):
    coefficients = list(map(int, coefficients.split()))
    
    return reduce(lambda a, item: a + item[1]*(x**(len(coefficients) - item[0] - 1)), enumerate(coefficients), 0)

print(evaluate(input(), int(input())))
