ip = list(int(_) for _ in input().split('.'))

print('ДА' if int(min(ip)) >= 0 and int(max(ip)) <= 255 else 'НЕТ')