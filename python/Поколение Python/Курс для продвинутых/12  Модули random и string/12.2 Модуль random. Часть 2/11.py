from random import randint, sample

numbers = sample(range(1, 76), 25)
numbers[12] = 0 

for i in range(5):
    print(*(_.ljust(3) for _ in map(str, numbers[i * 5:i * 5 + 5])))