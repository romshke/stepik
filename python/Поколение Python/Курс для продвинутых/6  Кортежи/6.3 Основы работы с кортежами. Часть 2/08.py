a, b, c = int(input()), int(input()), int(input())

def vertex(a, b, c):
    return -b / (2 * a), (4 * a * c - b**2) / (4 * a)

print(vertex(a, b, c))