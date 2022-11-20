from random import randint
from sys import maxsize


def dec_2_bin(number):
    result = str()

    while number // 2 > 0:
        result += str(number % 2)
        number = number // 2

    result += str(number)

    return result[::-1]

print(dec_2_bin(513)) 

n = randint(0, maxsize)
print(n, dec_2_bin(n))