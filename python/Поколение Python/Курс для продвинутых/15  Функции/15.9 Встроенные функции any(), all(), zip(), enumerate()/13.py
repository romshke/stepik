password = input()

print('YES' if all([*map(lambda _: any(_), zip(*map(lambda symbol: (symbol.isdigit(), symbol.upper() == symbol and not symbol.isdigit(), symbol.lower() == symbol and not symbol.isdigit()), password))), len(password) >= 7]) else 'NO')