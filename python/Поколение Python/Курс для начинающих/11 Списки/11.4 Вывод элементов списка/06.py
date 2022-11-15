l = list()

for _ in range(int(input())): l.append(input())
request = input()

for _ in l:
    if request.lower() in _.lower(): print(_)