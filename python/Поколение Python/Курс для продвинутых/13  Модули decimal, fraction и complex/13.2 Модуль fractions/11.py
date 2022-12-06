from fractions import Fraction
from math import factorial

print(sum(Fraction(1, factorial(_)) for _ in range(1, int(input()) + 1)))