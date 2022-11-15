n = int(input())
tmp = 0

while len(str(n)) > 1:
    for _ in str(n):
        tmp += int(_)
    n = tmp
    tmp = 0
print(n)