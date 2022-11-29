numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
def mul(tuple):
    result = tuple[0]
    
    for _ in tuple[1:]:
      result *= _
    
    return result
    
print(mul(numbers))