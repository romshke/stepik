l = list()

for _ in range(int(input())): l.append(int(input()))

l.remove(min(l))
l.remove(max(l))

print(*l, sep='\n')