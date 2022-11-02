a, b =  int(input()), int(input())
count = 0

for _ in range(a, b+1): 
    if str(_**3)[-1] == "4" or str(_**3)[-1] == "9": count+=1
print(count)