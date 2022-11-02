n = int(input())
total = 0

for _ in range(1, n+1):
    if str(_**2)[-1] == '2' or str(_**2)[-1] == '5' or str(_**2)[-1] == '8': total += _
print(total)