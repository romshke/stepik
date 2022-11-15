n = int(input())
res = '1 1 2'
previous = 1
current = 2 

if n == 1:
        print(1)
elif n == 2:
    print(1, 1)
elif n == 3:
    print(1, 1, 2)
else:
    for _ in range(4, n+1):
        temp = current
        current = previous + current
        previous = temp
        res += f" {current}"
    print(res)