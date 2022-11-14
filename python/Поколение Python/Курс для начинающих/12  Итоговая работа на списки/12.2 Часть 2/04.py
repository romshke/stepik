try:
    l = [int(_) for _ in input().split('-')]

    if len(l) == 4 and l[0] == 7 and len(str(l[1])) == 3 and len(str(l[2])) == 3 and len(str(l[3])) == 4: print('YES')
    elif len(l) == 3 and len(str(l[0])) == len(str(l[1])) == 3 and len(str(l[2])) == 4: print('YES')
    else: print('NO')
except:
    print('NO')