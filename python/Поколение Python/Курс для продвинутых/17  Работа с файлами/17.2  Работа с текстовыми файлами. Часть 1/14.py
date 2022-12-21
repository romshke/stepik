file = open('numbers.txt')

print(sum(map(int, file.readlines())))

file.close()