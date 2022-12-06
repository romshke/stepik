l = input().split()
n = int(input())

def chunked(l, n):
    result = list()

    for i in range(0, len(l), n):
        result.append(l[i:i+n])

    return result

print(chunked(l, n))