from random import randrange

for _ in range(int(input())):
    print('Орел' if randrange(2) == 0 else 'Решка')