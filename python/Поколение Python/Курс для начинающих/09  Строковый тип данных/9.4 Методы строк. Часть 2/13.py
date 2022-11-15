s = input()
letter = ''
count = 0

for _ in s:
    if s.count(_) >= count:
        count = s.count(_)
        letter = _

print(letter)