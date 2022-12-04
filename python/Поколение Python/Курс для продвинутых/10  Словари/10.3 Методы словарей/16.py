ids = input().split()

ids_dict = {}

for index, item in enumerate(ids):
    if item not in ids_dict:
        ids_dict.setdefault(item, ids[:index + 1].count(item))
    else:
        ids_dict.setdefault(f'{item}_{ids[:index].count(item)}', ids[:index + 1].count(item))
        
print(*ids_dict)