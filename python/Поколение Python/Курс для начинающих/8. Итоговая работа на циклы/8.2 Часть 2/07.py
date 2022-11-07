for a in range(1, 100):
    for b in range(a, 100):
        for c in range(a, 100):
            for d in range(a, 100):
                if a**3 + b**3 == c**3 + d**3 and a != b and a != c and a != d and b != c and b != d and c != d: print(a, b, c, d, a**3 + b**3, c**3 + d**3)