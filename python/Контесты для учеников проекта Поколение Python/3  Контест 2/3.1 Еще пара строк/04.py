number = input()
flag = True

while int(number) > 1:
    if sum(map(lambda _: int(_)**2, number)) == 4:
        flag = False
        break
    
    number = str(sum(map(lambda _: int(_)**2, number)))
    # print(number)

print('YES' if flag else 'NO')