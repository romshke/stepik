m, n = int(input()), int(input())
math_and_it = []

for _ in range(m + n):
    math_and_it.append(input())
   
print(n + m - (len(math_and_it) - len(set(math_and_it))) * 2 if n + m - (len(math_and_it) - len(set(math_and_it))) * 2 != 0 else 'NO')