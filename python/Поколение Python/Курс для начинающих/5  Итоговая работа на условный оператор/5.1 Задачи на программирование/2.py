a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

def color(a,b):
    if a%2 != 0:
        if b%2 != 0: return("white")
        else: return("black")
    elif a%2 == 0:
        if b%2 == 0: return("white")
        else: return("black")

if color(a1, b1) == color(a2, b2): print("YES")
else: print("NO")