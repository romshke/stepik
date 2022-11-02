res = True

for _ in range(10):
    if int(input())%2 != 0:
        res = False
        break
if res: print("YES")
else: print("NO")