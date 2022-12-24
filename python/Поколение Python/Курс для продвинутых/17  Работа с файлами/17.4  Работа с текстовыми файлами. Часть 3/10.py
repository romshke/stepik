from random import randint

with open('input.txt') as file:
    lines = file.readlines()
    
with open('output.txt', 'w') as file:
    file.writelines([f'{index + 1}) {value}' for index, value in enumerate(lines)])