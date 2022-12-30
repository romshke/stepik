n = [_ for _ in input()]

try:
    n[n.index('6')] = '9'
    print(*n, sep='')
except:
    print(*n, sep='')