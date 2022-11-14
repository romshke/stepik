def quick_merge(n, lists):
    subresult = lists[0]
    
    for _ in range(1, n):
        result = []
        p1 = 0
        p2 = 0

        while p1 < len(subresult) and p2 < len(lists[_]):
            if subresult[p1] <= lists[_][p2]:
                result.append(subresult[p1])
                p1 += 1
            else:
                result.append(lists[_][p2])
                p2 += 1

        if p1 < len(subresult):
            result += subresult[p1:]
        if p2 < len(lists[_]):
            result += lists[_][p2:]

        subresult = result.copy()

    return result

n = int(input())
lists = list()
for i in range(n): lists.append([int(j) for j in input().split()])

print(*quick_merge(n, lists))