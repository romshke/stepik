shopping_lists = {}

for _ in range(int(input())):
    tmp = input().split()

    if tmp[0] not in shopping_lists:
        shopping_lists.setdefault(tmp[0], {tmp[1]: int(tmp[2])})
    else:
        if tmp[1] not in shopping_lists[tmp[0]]:
            shopping_lists[tmp[0]].update({tmp[1]: int(tmp[2])})
        else:
            shopping_lists[tmp[0]][tmp[1]] += int(tmp[2])
    
for shopping_list in sorted(shopping_lists.items()):
    print(f'{shopping_list[0]}:')
    
    for item in sorted(shopping_list[1].items()):
        print(*item)