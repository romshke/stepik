substring, string = input(), input()

print('YES' if ''.join(map(lambda _: _ if _ in substring else '', string)).find(substring) != -1 and substring != string else 'NO')