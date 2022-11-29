string = input()

print('YES' if len(string) == len(set(string)) else 'NO')