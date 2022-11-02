n = input()
total_sum = 0
total_mul = 1

for _ in n[::]:
    total_sum += int(_)
    total_mul *= int(_)
print(total_sum, len(n), total_mul, total_sum/len(n), n[0], int(n[0]) + int(n[-1]), sep='\n')