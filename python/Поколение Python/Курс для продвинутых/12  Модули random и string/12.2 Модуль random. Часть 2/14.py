from random import choice, shuffle
from string import ascii_letters, ascii_uppercase, digits, ascii_lowercase

def generate_password(length):
    password = []
    
    while len(password) != length:
        sequence = list(_ for _ in (ascii_letters + digits) if _ not in 'lI1oO0')
        password += [choice(list(_ for _ in digits if _ not in 'lI1oO0')), choice(list(_ for _ in ascii_lowercase if _ not in 'lI1oO0')), choice(list(_ for _ in ascii_uppercase if _ not in 'lI1oO0'))]
        
        if len(password) < length:
            password.append(choice(sequence))
            
    shuffle(password) 
            
    return ''.join(password)

def generate_passwords(count, length):
    passwords = []
    
    for _ in range(count):
        passwords.append(generate_password(length))
        
    return passwords

n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')