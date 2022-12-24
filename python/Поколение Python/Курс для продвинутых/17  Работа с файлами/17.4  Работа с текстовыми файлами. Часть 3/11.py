from random import randint

with open('class_scores.txt') as file1, open('new_scores.txt', 'w') as file2:
    class_scores = list(map(str.split, file1))
    
    new_scores = list(map(lambda index, item: f'{item[0]} {int(item[1]) + 5 if int(item[1]) + 5 <= 100 else 100}\n' if index < len(class_scores) - 1 else f'{item[0]} {int(item[1]) + 5 if int(item[1]) + 5 <= 100 else 100}', range(len(class_scores)), class_scores))
    
    file2.writelines(new_scores)