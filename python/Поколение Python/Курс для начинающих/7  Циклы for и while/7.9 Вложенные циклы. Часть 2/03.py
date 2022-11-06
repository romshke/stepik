a, b = int(input()), int(input())
number, total, subtotal = None, 0, 0

for i in range(b, a, -1):
    for j in range(1, b+1):
        if i % j == 0: subtotal += j
    if subtotal > total:
        total = subtotal
        number = i
    subtotal = 0
print(number, total)