n = int(input())

for i in range(n):
    if i == 0 or i == n-1: print('*' * 19)
    else: print(f"*{' ' * 17}*")