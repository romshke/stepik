digits = list(int(_) for _ in input()) + list(int(_) for _ in input())

print('YES' if len(set(digits)) == 10 else 'NO')