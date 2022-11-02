m, n =  int(input()), int(input())

if m < n: 
    for _ in range(m, n+1): print(_)
else:
    for _ in range(m, n-1, -1): print(_)