l, requests = list(), list()

for _ in range(int(input())): l.append(input())
for _ in range(int(input())): requests.append(input())

for i in l:
    flag = True
    for j in requests:
        if j.lower() not in i.lower():
            flag = False
            break
    if flag: print(i)