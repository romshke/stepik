for _ in range(int(input())):
    if _ == 0:
        s = set(map(int, set(input())))
    else: 
        s.intersection_update(set(map(int, set(input()))))

print(*sorted(s))