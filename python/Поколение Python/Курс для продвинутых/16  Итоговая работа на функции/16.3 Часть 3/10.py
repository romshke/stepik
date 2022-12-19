words = {}

for _ in range(int(input())):
    word = input()
    words.setdefault(word, sum(map(lambda _: ord(_) - ord('A'), word.upper())))
    
print(*sorted(sorted(words), key=lambda _: words[_]), sep='\n')