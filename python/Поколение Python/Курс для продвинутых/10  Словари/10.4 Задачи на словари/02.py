word = input()
d1 = {_: word.count(_) for _ in set(word)}

word = input()
d2 = {_: word.count(_) for _ in set(word)}

print('YES' if d1 == d2 else 'NO')