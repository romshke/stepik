m, n =  int(input()), int(input())

for _ in range(m, n+1): 
    if _%17 == 0 or str(_)[-1] == '9' or (_%3 == 0 and _%5 == 0): print(_)