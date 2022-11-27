cell = list()

for _ in input():
    if _.isalpha():
        cell.append(ord(_) - ord('a'))
    else:
        cell.append(int(_) - 1)

board = [['.' for _ in range(8)] for _ in range(8)]

# print(board)

for i in range(8):
    for j in range(8):
        if i == cell[1]:
            board[i][j] = '*'
        if j == cell[0]:
            board[i][j] = '*'
        if cell[0] + i == cell[1] + j:
            board[i][j] = '*'
        if abs(cell[1] - i) == abs(cell[0] - j):
            board[i][j] = '*'
        if i == cell[1] and j == cell[0]:
            board[i][j] = 'Q'

for _ in range(8):
    print(*board[7 - _])