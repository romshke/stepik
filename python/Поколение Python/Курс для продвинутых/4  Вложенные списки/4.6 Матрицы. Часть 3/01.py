n, m = list(map(int, input().split()))
board = [['' for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i % 2 == 0 and j % 2 == 0:
            board[i][j] = '.'
        elif i % 2 == 0 and j % 2 != 0:
            board[i][j] = '*'
        elif i % 2 != 0 and j % 2 == 0:
            board[i][j] = '*'
        elif i % 2 != 0 and j % 2 != 0:
            board[i][j] = '.'
        
for i in range(n):
    print(*board[i])