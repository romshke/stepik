with open(input()) as file:
    lines = file.readlines()
    result = []
    
    for index, line in enumerate(lines):
        try:
            if 'def' in line and '#' not in lines[index - 1]:
                result.append(line[line.find('def ') + 4:line.find('(')])
        except:
            pass
        
    print('Best Programming Team') if result == [] else print(*result, sep='\n')