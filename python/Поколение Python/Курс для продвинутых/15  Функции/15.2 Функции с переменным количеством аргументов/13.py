def greet(name, *args):
    result = 'Hello, ' + name
    
    for _ in args:
        result += ' and ' + _

    return result + '!'

# def greet(name, *args):
#     return f'Hello, {" and ".join((name,) + args)}!'

print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))