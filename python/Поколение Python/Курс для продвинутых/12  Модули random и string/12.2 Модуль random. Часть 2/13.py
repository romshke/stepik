from random import choice
from string import ascii_letters, digits

def generate_password(length):
    password = str()
    
    for _ in range(length):
        password += choice(list(_ for _ in (ascii_letters + digits) if _ not in 'lI1oO0'))

    return password

def generate_passwords(count, length):
    passwords = []
    
    for _ in range(count):
        passwords.append(generate_password(length))
        
    return passwords

n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')