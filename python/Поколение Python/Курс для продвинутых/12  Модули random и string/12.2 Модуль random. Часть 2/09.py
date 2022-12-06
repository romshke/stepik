from random import randint

numbers = set()

while len(numbers) != 100:
    numbers.add(int(f'{randint(1, 9)}' + ''.join(f'{randint(0, 9)}' for _ in range(6))))
    
print(*numbers, sep='\n')