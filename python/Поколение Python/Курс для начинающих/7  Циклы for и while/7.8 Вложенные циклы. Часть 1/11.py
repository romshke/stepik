for n in range(1, 365 // 28 + 1):
    for k in range(1, 365 // 30 + 1):
        for m in range(1, 365 // 31 + 1): 
            if 28 * n + 30 * k + 31 * m == 365: print(n, k, m)
