l = input()

print(l.replace(' ', '+'), '=', sum(int(_) for _ in l.split()), sep='')