from sys import maxsize

n = int(input())
result = [0, 0, 0, 0]

for i in range(n):
    l = list(map(int, input().split()))

    if n // 2 > i:
        # print(l[i + 1:n - i - 1])
        result[0] += sum(l[i + 1:n - i - 1])
        
        if i != 0:
            # print(l[-i:])
            result[1] += sum(l[-i:])
            
        # print(l[:i])
        result[3] += sum(l[:i])
        
    else:
        # print(l[:n - i - 1])
        result[3] += sum(l[:n - i - 1])
        
        # print(l[i + 1:])
        result[1] += sum(l[i + 1:])
        
        # print(l[n-i:i])
        result[2] += sum(l[n-i:i])

print(
    f'Верхняя четверть: {result[0]}',
    f'Правая четверть: {result[1]}',
    f'Нижняя четверть: {result[2]}',
    f'Левая четверть: {result[3]}',
    sep='\n'
)