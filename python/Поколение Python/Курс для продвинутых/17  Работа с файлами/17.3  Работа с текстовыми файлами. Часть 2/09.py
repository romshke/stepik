with open('lines.txt') as file:
    lines = file.readlines()
    print(*map(str.strip ,filter(lambda _: len(max(lines, key=len)) == len(_), lines)), sep='\n')