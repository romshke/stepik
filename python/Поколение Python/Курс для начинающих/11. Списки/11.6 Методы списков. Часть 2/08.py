l = list()

for _ in range(int(input()[1:])):
    s = input()
    if '#' in s: s = s.replace(s[s.find('#'):], '')
    s = s.rstrip()
    l.append(s)

print(*l, sep='\n')