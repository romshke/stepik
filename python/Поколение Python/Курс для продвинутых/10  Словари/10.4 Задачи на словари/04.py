synonyms = {}

for _ in range(int(input())):
    words = input().split()
    synonyms.setdefault(words[0], words[1])
    synonyms.setdefault(words[1], words[0])
    
print(synonyms[input()])