from fractions import Fraction

# result = Fraction(0)

# for _ in range(1, int(input()) + 1):
#     result += Fraction(1, _**2)
    
# print(result)

print(sum(Fraction(1, _**2) for _ in range(1, int(input()) + 1)))