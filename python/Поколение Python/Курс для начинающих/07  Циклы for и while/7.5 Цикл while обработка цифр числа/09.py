n = input()
i = 1

while i < len(n) and n[0] == n[i]:
    i+= 1
if i == len(n): print("YES")
else: print("NO")