processes = {'write': 'W', 'read': 'R', 'execute': 'X'}
files = {}

for _ in range(int(input())):
    tmp = input().split()
    
    files.setdefault(tmp[0], tmp[1:])

for _ in range(int(input())):
    tmp = input().split()
    
    print('OK' if processes[tmp[0]] in files[tmp[1]] else 'Access denied')