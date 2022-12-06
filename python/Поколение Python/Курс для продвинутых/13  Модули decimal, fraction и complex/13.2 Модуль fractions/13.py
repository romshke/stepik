from fractions import Fraction

n = int(input())
result = []

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if str(Fraction(i, j)) == f'{i}/{j}':
            result.append(Fraction(i, j))
        
print(*sorted(result), sep='\n')