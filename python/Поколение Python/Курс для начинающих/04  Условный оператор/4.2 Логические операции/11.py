x = int(input())

if (x // 1000 > 0 and x // 1000 < 10) and (x % 7 == 0 or x % 17 == 0):
    print('YES')
else:
    print('NO')