n = input()
if n[::-1] == ''.join(sorted(n[::])): print("YES")
else: print("NO")