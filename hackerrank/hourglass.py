def hourglassSum(arr):
    # Write your code here
    max_sum = float('-inf')
    summ = 0
    
    for i in range(0, 4):
        for j in range(0, 4):
            summ = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            summ = summ + arr[i + 1][j + 1]
            summ = summ + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            
            if summ > max_sum:
                max_sum = summ
        
    return max_sum

# arr = [
#     [-9, -9, -9,  1, 1, 1],
#     [ 0, -9,  0,  4, 3, 2],
#     [-9, -9, -9,  1, 2, 3],
#     [ 0,  0,  8,  6, 6, 0],
#     [ 0,  0,  0, -2, 0, 0],
#     [ 0,  0,  1,  2, 4, 0]
# ]
arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
print(hourglassSum(arr))