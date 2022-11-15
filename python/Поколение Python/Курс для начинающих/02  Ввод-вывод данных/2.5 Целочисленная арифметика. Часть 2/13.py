from functools import reduce


a = list(int(i) for i in input())
print("Сумма цифр =", sum(a))
print("Произведение цифр =", reduce((lambda x, y: x * y), a))