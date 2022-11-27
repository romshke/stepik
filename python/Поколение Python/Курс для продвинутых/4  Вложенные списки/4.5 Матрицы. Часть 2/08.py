cell = list()

for _ in input():
    if _.isalpha():
        cell.append(ord(_) - ord('a'))
    else:
        cell.append(int(_) - 1)

# print(cell)

board = [['.' for _ in range(8)] for _ in range(8)]

# print(board)

for i in range(8):
    for j in range(8):
        if (i == cell[1] + 2 and j == cell[0] + 1):
            board[i][j] = '*'
        if (i == cell[1] + 2 and j == cell[0] - 1):
            board[i][j] = '*'
        if (i == cell[1] - 2 and j == cell[0] + 1):
            board[i][j] = '*'
        if (i == cell[1] - 2 and j == cell[0] - 1):
            board[i][j] = '*'
        if (i == cell[1] + 1 and j == cell[0] + 2):
            board[i][j] = '*'
        if (i == cell[1] + 1 and j == cell[0] - 2):
            board[i][j] = '*'
        if (i == cell[1] - 1 and j == cell[0] + 2):
            board[i][j] = '*'
        if (i == cell[1] - 1 and j == cell[0] - 2):
            board[i][j] = '*'
        if (i == cell[1] and j == cell[0]):
            board[i][j] = 'N'
        
for _ in range(8):
    print(*board[7 - _])