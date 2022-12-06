set1 = set(map(int, set(input().split())))
set2 = set(map(int, set(input().split())))
set3 = set(map(int, set(input().split())))

print(*sorted(set(range(11)) - (set1 | set2 | set3)))