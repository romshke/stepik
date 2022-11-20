from random import randint
from sys import maxsize


def dec_2_hex(number):
    result = str()

    while number // 16 > 0:
        subresult = number % 16

        if subresult > 9:
            match subresult:
                case 10: result += 'A'
                case 11: result += 'B'
                case 12: result += 'C'
                case 13: result += 'D'
                case 14: result += 'E'
                case 15: result += 'F'
        else:
            result += str(subresult)

        number = number // 16

    result += str(number)

    return result[::-1]

print(dec_2_hex(1000))

n = randint(0, maxsize)
print(n, dec_2_hex(n))