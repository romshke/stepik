def print_products(*args):
    result = [f'{index + 1}) {product}' for index, product in enumerate(_ for _ in args if type(_) == str and _ != '')]
    print(*result if len(result) > 0 else ['Нет продуктов'], sep='\n')

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')