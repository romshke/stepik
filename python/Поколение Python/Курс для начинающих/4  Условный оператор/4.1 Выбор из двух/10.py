n1, n2, n3, n4 = int(input()), int(input()), int(input()), int(input())

min = (n1 if n1 < n2 else n2)
min = (min if min < n3 else n3)
min = (min if min < n4 else n4)
print(min)