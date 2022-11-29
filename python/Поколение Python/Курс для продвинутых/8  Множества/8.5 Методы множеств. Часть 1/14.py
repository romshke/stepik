s = set()

for _ in list(map(int, input().split())):
    print('YES' if _ in s else 'NO')
    s.add(_)