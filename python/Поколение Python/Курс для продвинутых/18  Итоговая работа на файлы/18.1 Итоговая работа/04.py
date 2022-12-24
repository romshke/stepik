with open('words.txt') as file:
    words = file.read().split()
    print(*filter(lambda _: len(_) == len(max(words, key=len)), words), sep='\n')
