'''
QUESTION -
Return the absolute difference of the sum of the diagonals of any given matrix
'''

def diagonalDifference(arr):
    n = len(arr)
    diag = 0
    antiDiag = 0
    summ = 0

    for i in range(n):
        diag = diag + arr[i][i]
        antiDiag = antiDiag + arr[i][(n - 1) - i]

    summ = abs(diag - antiDiag)
    
    return summ

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]
print(diagonalDifference(arr))

'''
TRACING :
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

n = len(arr)
n = 3

diag, antiDiag, summ = 0

for i in range(n):
    -> i = 0
    diag = diag + arr[i][i]
    diag = 0 + arr[0][0] -> 0 + 1
    diag = 1

    antiDiag = antiDiag + arr[i][(n - 1) - i]
    antiDiag = 0 + arr[0][(3 - 1) - 0]
    antiDiag = 0 + arr[0][2] -> 0 + 3
    antiDiag = 3

    -> i = 1
    diag = diag + arr[i][i]
    diag = 1 + arr[1][1] -> 1 + 5
    diag = 6

    antiDiag = antiDiag + arr[i][(n - 1) - i]
    antiDiag = 3 + arr[1][2 - 1]
    antiDiag = 3 + arr[1][1] -> 3 + 5
    antiDiag = 8

    -> i = 2
    diag = diag + arr[i][i]
    diag = 6 + arr[2][2] -> 6 + 9
    diag = 15

    antiDiag = antiDiag + arr[i][(n - 1) - i]
    antiDiag = 8 + arr[2][2 - 2]
    antiDiag = 8 + arr[2][0] -> 8 + 9
    antiDiag = 17

    -> i = 3 -> out of range, out of loop

summ = abs(diag - antiDiag)
summ = abs(15 - 17)
summ = abs(-2)

summ = 2

'''