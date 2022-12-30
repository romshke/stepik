from sys import maxsize

n, k = [_ for _ in input()], int(input())
m = str(maxsize)

for _ in range(k):
    for _ in range(len(n)):
        # print(n[:_] + n[_ + 1:])
        
        if int(m) > int(''.join(n[:_] + n[_ + 1:])):
            m = ''.join(n[:_] + n[_ + 1:])
            
    n = [_ for _ in m]
    
print(int(m))