with open('numbers.txt') as file:
    print(*map(sum, map(lambda _: map(int, _.split()), file.readlines())), sep='\n')