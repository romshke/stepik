from random import choice
from string import ascii_uppercase

def generate_index():
    return f'{choice(ascii_uppercase)}{choice(ascii_uppercase)}{choice(range(100))}_{choice(range(100))}{choice(ascii_uppercase)}{choice(ascii_uppercase)}'