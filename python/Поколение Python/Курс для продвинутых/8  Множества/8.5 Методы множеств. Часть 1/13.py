string = input().lower()

for _ in '.,;:-?!':
    string = string.replace(_, '')

print(len(set(string.split())))