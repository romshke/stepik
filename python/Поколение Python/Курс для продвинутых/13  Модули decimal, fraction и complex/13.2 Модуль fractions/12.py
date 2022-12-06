from fractions import Fraction

n = int(input())
result = Fraction(0)

for _ in range(1, n):
    if str(Fraction(_, n - _)) == f'{_}/{n - _}' and Fraction(_, n - _) < 1:
        result = max(result, Fraction(_, n - _))
        
print(result)