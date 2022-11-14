l = [int(_) for _ in input().split()]
nl = list()
nl = l.copy()
mx, mn = max(l), min(l)

nl[l.index(mx)] = mn
nl[l.index(mn)] = mx

print(*nl)