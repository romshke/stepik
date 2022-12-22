from random import choice

with open('first_names.txt') as file:
    first_names = file.readlines()

with open('last_names.txt') as file:
    last_names = file.readlines()
    
for _ in range(3):
    fn = choice(first_names)
    ln = choice(last_names)
    
    print(f'{fn.strip()} {ln.strip()}')
    
    first_names.remove(fn), last_names.remove(ln)
    