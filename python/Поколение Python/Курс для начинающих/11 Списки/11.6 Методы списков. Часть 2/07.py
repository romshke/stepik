count = 0
for _ in input().lower().split():
    if _ in ['a', 'an', 'the']: count += 1

print(f"Общее количество артиклей: {count}")