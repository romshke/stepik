file = open('prices.txt')

shoppinglist = [list(map(lambda item: int(item) if item.isdigit() else item, _.split())) for _ in file.readlines()]

print(sum(_[1] * _[2] for _ in shoppinglist))

file.close()