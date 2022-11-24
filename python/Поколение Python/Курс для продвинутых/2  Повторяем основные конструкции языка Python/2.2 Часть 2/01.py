n = int(input())

counts = [0, 0, 0, 0]

for _ in range(n):
    x, y = map(int, input().split())

    if x > 0 and y > 0: counts[0] += 1
    if x < 0 and y > 0: counts[1] += 1
    if x < 0 and y < 0: counts[2] += 1
    if x > 0 and y < 0: counts[3] += 1

print(f'Первая четверть: {counts[0]}', f'Вторая четверть: {counts[1]}', f'Третья четверть: {counts[2]}', f'Четвертая четверть: {counts[3]}', sep='\n')