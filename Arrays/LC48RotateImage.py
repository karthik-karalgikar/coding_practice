def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for k in range(len(matrix)):
        matrix[k].reverse()

    return matrix

print(rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

'''
TRACING - 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

len(matrix) = 3
len(matrix[0]) = 3

for i in range(len(matrix)):
    -> i = 0
    for j in range(i + 1, len(matrix[0])):
        -> j = 1
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        [0][1], [1][0] = [1][0], [0][1]
        2, 4 = 4, 2

        -> j = 2
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        [0][2], [2][0] = [2][0], [0][2]
        3, 7 = 7, 3

    -> i = 1
        -> j = 2
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        [1][2], [2][1] = [2][1], [1][2]
        6, 8 = 8, 6
    
    -> i = 2
        j = 3 -> out of loop

    now matrix is like - 
    matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    for k in range(len(matrix)):
        -> k = 0
        matrix[k].reverse()
        matrix[0].reverse()
        [1, 4, 7] -> [7, 4, 1]

        -> k = 1
        matrix[1].reverse()
        [2, 5, 8] -> [8, 5, 2] 

        -> k = 2
        matrix[2].reverse()
        [3, 6, 9] -> [9, 6, 3]

    return matrix

Output - [[7, 4, 1], [8, 5, 2], [9, 6, 3]]



'''