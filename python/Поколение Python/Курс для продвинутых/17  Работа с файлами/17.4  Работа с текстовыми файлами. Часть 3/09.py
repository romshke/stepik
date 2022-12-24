from random import randint

with open('random.txt', 'w') as file:
    file.writelines([str(randint(111, 777)) + '\n' for _ in range(25)])