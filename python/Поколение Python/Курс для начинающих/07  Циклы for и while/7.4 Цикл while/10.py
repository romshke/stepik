count = 0
word = input()

while word != "стоп" and word != "хватит" and word != "достаточно": 
    count += 1
    word = input()
print(count)