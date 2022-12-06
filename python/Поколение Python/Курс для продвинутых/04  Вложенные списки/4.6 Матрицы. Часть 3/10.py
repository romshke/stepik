rows, columns = map(int, input().split())
matrix = [[0 for _ in range(columns)] for i in range(rows)]

is_horizontal = True
is_left_2_right_direction = True

rows_top, rows_bottom = 0, rows
columns_left, columns_right = 0, columns
number = 1

while number <= rows * columns:
    if is_horizontal and is_left_2_right_direction:
        # print('#1', rows_top, rows_bottom, columns_left, columns_right)

        for _ in range(columns_left, columns_right):
            matrix[rows_top][_] = number
            number += 1
        
        rows_top += 1
        columns_right -= 1

        is_horizontal = False
        is_left_2_right_direction = True
        
        # input()

    elif not is_horizontal and is_left_2_right_direction:
        # print('#2', rows_top, rows_bottom, columns_left, columns_right)
        
        for _ in range(rows_top, rows_bottom):
            matrix[_][columns_right] = number
            number += 1
         
        rows_bottom -= 1
        columns_right -= 1
        
        is_horizontal = True
        is_left_2_right_direction = False
        
        # input()
        
    elif is_horizontal and not is_left_2_right_direction: 
        # print('#3', rows_top, rows_bottom, columns_left, columns_right)
        
        for _ in range(columns_right, columns_left - 1, - 1):
            matrix[rows_bottom][_] = number
            number += 1
        
        rows_bottom -= 1
        
        is_horizontal = False
        is_left_2_right_direction = False
        
        # input()
        
        
    elif not is_horizontal and not is_left_2_right_direction:  
        # print('#4', rows_top, rows_bottom, columns_left, columns_right)
        
        for _ in range(rows_bottom, rows_top - 1, - 1):
            matrix[_][columns_left] = number
            number += 1
        
        columns_left += 1
        rows_bottom += 1
        columns_right += 1
        
        is_horizontal = True
        is_left_2_right_direction = True
        
        # input()
    
for i in range(len(matrix)):
    print(*list(str(_).ljust(3) for _ in matrix[i]))