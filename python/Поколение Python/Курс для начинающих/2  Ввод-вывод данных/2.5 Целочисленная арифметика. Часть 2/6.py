import math

b1 = int(input())
q = int(input())
n = int(input())

def bn(_b1, _q, _n):
    return int(_b1 * math.pow(_q, (_n - 1)))

print(bn(b1, q, n))