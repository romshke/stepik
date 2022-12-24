titles = [input() for _ in range(int(input()))]  
    
with open('output.txt', 'w') as output:  
    for title in titles:
        with open(title) as file:
            output.write(file.read())