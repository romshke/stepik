n = int(input())
total, subtotal = 0, 1

for i in range(1, n+1):
    subtotal *= i
    total += subtotal

print(total)