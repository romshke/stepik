n1, n2, n3 = int(input()), int(input()), int(input())

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('YES')
else:
    print('NO')