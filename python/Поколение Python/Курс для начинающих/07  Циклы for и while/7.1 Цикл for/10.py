m, p, n = float(input()), int(input()), int(input())

print(1, m)
for i in range(1, n): 
    m = m+m*p/100
    print(i+1, m)