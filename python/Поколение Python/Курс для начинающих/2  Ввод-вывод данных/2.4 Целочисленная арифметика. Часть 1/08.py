import math


def f(a,b):
    return int(3*math.pow((a+b),3)+275*math.pow(b,2)-127*a-41)

_a = int(input())
_b = int(input())

print(f(_a,_b))