m, n = int(input()), int(input())
home_books_list = set()

for _ in range(m):
    home_books_list.add(input())
    
for _ in range(n):
    print('YES' if input() in home_books_list else 'NO')