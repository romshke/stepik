with open(input()) as file:  
    print(*map(lambda _: _.replace('\n', ''),file.readlines()[-10:]), sep='\n')
