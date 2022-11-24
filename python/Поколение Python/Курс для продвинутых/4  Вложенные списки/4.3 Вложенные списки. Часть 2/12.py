string = input().split()
result = list()
subresult = [string[0][:]]

for _ in range(1, len(string)):
   if string[_] in subresult:
      subresult.append(string[_])
   else:
      result.append(subresult)
      subresult = [string[_][:]]

result.append(subresult)   

print(result)