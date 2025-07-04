def searchMatrix(matrix, target):
    row = len(matrix)
    col = len(matrix[0])

    low = 0
    high = (row * col) - 1

    while low <= high:
        mid = (low + high) // 2
        r = int(mid / col)
        c = mid % col
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))

'''
TRACING :
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

row = len(matrix) 
row = 3

col = len(matrix[0])
col = 4

low = 0
high = row * col - 1 -> 3 * 4 - 1
high = 11

The quotient (index // cols) tells you which row you're in.
The remainder (index % cols) tells you which column you're at in that row.

while low <= high:
    0 <= 11 -> true
    mid = low + high // 2 -> 0 + 11 // 2
    mid = 5

    r = int(mid / col)
    r = int (5 / 4)
    r = 1

    c = mid % col
    c = 5 % 4
    c = 1

    if matrix[r][c] == target:
        mattix[1][1] = 11 -> false

    elif matrix[r][c] < target :
        11 < 3 -> false

    else:
        high = mid - 1 -> 5 - 1
        high = 4

low = 0
high = 4
while low <= high: -> true
    mid = low + high // 2
    mid = 2
        
    r = int(mid / col)
    r = int(2 / 4)
    r = 0

    c = mid % col
    c = 2 % 4
    c = 2

    if matrix[r][c] == target:
        matrix[0][2] = 5 -> false
    
    elif matrix[r][c] < target:
        5 < 3 -> false
    
    else:
        high = mid - 1
        high = 1

low = 0
high = 1
while low <= high: -> true
    mid = low + high // 2
    mid = 1

    r = int(mid / col)
    r = int (1 / 4)
    r = 0

    c = mid % col
    c = 1 % 4
    c = 1
    
    if matrix[r][c] == target:
        matrix[0][1] = 3 == target -> true
        return True


'''