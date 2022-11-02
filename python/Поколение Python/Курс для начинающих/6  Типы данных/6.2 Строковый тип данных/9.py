a, b, c = input(), input(), input()

if (sorted([len(a), len(b), len(c)])[2] - sorted([len(a), len(b), len(c)])[1] == sorted([len(a), len(b), len(c)])[1] - sorted([len(a), len(b), len(c)])[0]): print("YES")
else: print("NO")