s = input() + ' запретил букву '

for letter in range(ord('а'), ord('я') + 1):
    if chr(letter) in s:
        s += chr(letter)
        s = s.strip()
        if len(s) > 1:
            print(s)
        for _ in s:
            s = s.replace(chr(letter), '')
            if '  ' in s:
                s = s.replace('  ', ' ')