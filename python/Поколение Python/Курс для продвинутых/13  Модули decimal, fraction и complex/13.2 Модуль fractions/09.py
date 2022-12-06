from fractions import Fraction

n1 = input()
n2 = input()

print(
    f'{n1} + {n2} = {Fraction(n1) + Fraction(n2)}',
    f'{n1} - {n2} = {Fraction(n1) - Fraction(n2)}',
    f'{n1} * {n2} = {Fraction(n1) * Fraction(n2)}',
    f'{n1} / {n2} = {Fraction(n1) / Fraction(n2)}',
    sep='\n'
)