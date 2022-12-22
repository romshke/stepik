import string

with open('file.txt') as file:
    lines = [''.join(map(lambda _: _ if _ not in string.punctuation else ' ', line)).strip().split() for line in file]
    
    print(f'Input file contains:\n{sum([sum([len([letter for letter in word if not letter.isdigit()]) for word in line]) for line in lines])} letters\n{sum(len(line) for line in lines)} words\n{len(lines)} lines')