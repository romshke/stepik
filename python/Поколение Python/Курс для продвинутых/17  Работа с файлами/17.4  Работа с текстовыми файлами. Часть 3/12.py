with open('goats.txt') as file1, open('answer.txt', 'w') as file2:  
    lines = list(map(lambda _: _.replace('\n', ''), file1.readlines()))
    goats = lines[lines.index('GOATS') + 1:]
    
    print(*[color for color, count in map(lambda _: (_, goats.count(_)), set(goats)) if count > len(goats)*0.07], sep='\n', file=file2)