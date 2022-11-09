n, s = int(input()), input()

for _ in s: 
    if ord(_) - n < 97: print(chr(ord(_) - n + 26), end='')
    else: print(chr(ord(_) - n), end='')