import re

numbers = []

for _ in range(int(input())):
    number = input()
    
    if re.fullmatch('\d{3}-\d{3}-\d{4}|\(\d{3}\)\s\d{3}-\d{4}', number):
        numbers.append(number)
        
print(*numbers if numbers != [] else ('All phone numbers are incorrect',), sep='\n')