from random import choice

file = open('lines.txt')

print(choice(file.readlines()))

file.close()