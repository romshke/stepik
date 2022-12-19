from math import sin

def f(n, func):
    functions = {
        'квадрат': n**2,
        'куб': n**3,
        'корень': n**0.5,
        'модуль': abs(n),
        'синус': sin(n),
    }
    
    return functions[func]

print(f(int(input()), input()))