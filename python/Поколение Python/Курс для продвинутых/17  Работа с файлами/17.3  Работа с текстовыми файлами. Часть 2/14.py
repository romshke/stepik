with open('population.txt') as file:
    print(
        *(_[0] for _ in filter(lambda _: _[0][0] == 'G' and _[1] > 500000, [list(map(lambda _: int(_) if _.isdigit() else _, line.strip().split('\t'))) for line in file])), sep='\n'
    )