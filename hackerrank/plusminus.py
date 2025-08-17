'''
QUESTION -

'''

def plusMinus(arr):
    # Write your code here
    countPos = 0
    countNeg = 0
    countZero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            countPos = countPos + 1
        elif arr[i] < 0: 
            countNeg = countNeg + 1
        else:
            countZero = countZero + 1
            
    return list([countPos/len(arr), countNeg/len(arr), countZero/len(arr)])

arr = [1, 1, 0, -1, -1]
for numbers in plusMinus(arr):
    print(f"{numbers:.6f}")
# print(plusMinus(arr))