word = input()

symbols = {word.count(_): _ for _ in set(word)}

decryption = {}

for _ in range(int(input())):
    tmp = input().split(': ')
    decryption.setdefault(symbols[int(tmp[1])], tmp[0])
    
for _ in decryption.items():
    word = word.replace(_[0], _[1])
    
print(word)