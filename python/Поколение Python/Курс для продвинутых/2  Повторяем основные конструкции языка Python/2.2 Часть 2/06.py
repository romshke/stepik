n = int(input())
l = list(int(input()) for _ in range(n))
mul = int(input())
result = False

for i in range(n):
    for j in range(i + 1, n):
        if l[i]*l[j] == mul:
            result = True

print('ДА' if result else 'НЕТ')