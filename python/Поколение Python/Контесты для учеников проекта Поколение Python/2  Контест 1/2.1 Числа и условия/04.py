a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(a + abs(b - d) * c if (b - d) < 0 else a)