n1, n2, n3 = int(input()), int(input()), int(input())
sum = 0

sum = (sum + n1 if n1 > 0 else sum)
sum = (sum + n2 if n2 > 0 else sum)
sum = (sum + n3 if n3 > 0 else sum)
print(sum)