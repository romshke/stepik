n = int(input())
t1, t2, t3 = 0, 1, 1
for i in range(n):
    # print(t1, end = ' ')
    t1, t2, t3 = t2, t3, t1 + t2 + t3
    
print(t1)