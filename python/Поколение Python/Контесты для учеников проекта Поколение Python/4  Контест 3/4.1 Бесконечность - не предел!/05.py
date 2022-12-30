string = [_ for _ in input()]
reversed_letters = [_ for _ in string[::-1] if _.isalpha()]
i = 0

for _ in range(len(string)):
    if string[_].isalpha():
        string[_] = reversed_letters[i]
        i += 1
        
print(*string, sep='')