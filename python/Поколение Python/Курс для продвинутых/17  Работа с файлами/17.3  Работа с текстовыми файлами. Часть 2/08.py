with open('data.txt') as file:
    print(*map(str.strip, file.readlines()[::-1]), sep='\n')