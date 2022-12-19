def arithmetic_operation(operation):
    # match operation:
    #     case '+': return lambda x, y: x + y
    #     case '-': return lambda x, y: x - y
    #     case '*': return lambda x, y: x * y
    #     case '/': return lambda x, y: x / y
        
    return {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}[operation]

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))