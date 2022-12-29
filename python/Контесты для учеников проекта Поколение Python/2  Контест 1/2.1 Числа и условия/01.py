number = input()

print('YES' if any(map(lambda _: number[_ - 1] == number[_], range(1, len(number)))) else 'NO')