m, n = int(input()), int(input())
math, it = set(), set()

for _ in range(m):
    math.add(input())
    
for _ in range(n):
    it.add(input())
    
print(len(math.symmetric_difference(it)) if len(math.symmetric_difference(it)) != 0 else 'NO')