n, k = int(input()), int(input())

l = list(_ for _ in range(1, n + 1))

count = 1

while len(l) > 1:
    for i in range(len(l)):
        if count == k:
            l.extend(l[:i + 1])
            del l[:i + 1]
            l.pop()
            count = 1
            break
        else:
            count += 1
print(*l)