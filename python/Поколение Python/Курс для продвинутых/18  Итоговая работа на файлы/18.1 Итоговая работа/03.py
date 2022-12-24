with open('grades.txt') as file:  
    print(
        len([item[0] for item in [list(map(lambda _: int(_) if _.isdigit() else _, line.split())) for line in file] if item[1] >= 65 and item[2] >= 65 and item[3] >= 65])
    )
