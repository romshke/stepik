contacts = {}

for _ in range(int(input())):
    contact = input().lower().split()
    contacts.setdefault(contact[1], [contact[0]]) if contact[1] not in contacts else contacts[contact[1]].append(contact[0])

for _ in range(int(input())):
    name = input().lower()
    if name in contacts:
        print(*contacts[name])
    else:
        print('абонент не найден')