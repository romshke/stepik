from sys import maxsize

n, Max, Min = input(), -maxsize, maxsize

for _ in n:
    Max = max(Max, int(_))
    Min = min(Min, int(_))
print(f"Максимальная цифра равна {Max}", f"Минимальная цифра равна {Min}", sep='\n')