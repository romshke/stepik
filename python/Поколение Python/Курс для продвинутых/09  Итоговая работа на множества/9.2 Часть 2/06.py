set1, set2 = set(map(int, input().split())), set(map(int, input().split()))

if len(set1 & set2) == 0:
    print('BAD DAY')
else:
    print(*sorted(set1 & set2, reverse=True))