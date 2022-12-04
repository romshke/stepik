word = input().lower()
d1 = {_: word.count(_) for _ in set(word) if _ not in '.,!?:;- '}

word = input().lower()
d2 = {_: word.count(_) for _ in set(word) if _ not in '.,!?:;- '}

print('YES' if d1 == d2 else 'NO')