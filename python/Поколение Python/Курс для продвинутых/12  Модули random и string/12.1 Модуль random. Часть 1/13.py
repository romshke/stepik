from random import choice

print(*(chr(choice(list(range(ord('A'), ord('Z') + 1)) + list(range(ord('a'), ord('z') + 1)))) for _ in range(int(input()))), sep='')