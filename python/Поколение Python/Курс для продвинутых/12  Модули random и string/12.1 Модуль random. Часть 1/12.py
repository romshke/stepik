from random import randrange

print(*(randrange(1, 7) for _ in range(int(input()))), sep='\n')