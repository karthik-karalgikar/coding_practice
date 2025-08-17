'''
QUESTION - 
given an array, calculate the max and min sums of the integers of the array by summing exactly n-1 of n integers
'''

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    summ = 0
    for i in range(len(arr)):
        summ = summ + arr[i]
        
    maxSum = summ - arr[0]
    minSum = summ - arr[len(arr) - 1]
    
    print(minSum, maxSum)

miniMaxSum(arr=[1, 3, 5, 7, 9])

'''
TRACING : 

arr = [1, 3, 5, 7, 9]
arr.sort()
arr = [1, 3, 5, 7, 9]
summ = 0
for i in range(len(arr)):
    -> i = 0
    summ = summ + arr[0] -> 0 + 1
    summ = 1

    -> i = 1
    summ = summ + arr[1] -> 1 + 3
    summ = 4

    -> i = 2
    summ = summ + arr[2] -> 4 + 5
    summ = 9

    -> i = 3
    summ = summ + arr[3] -> 9 + 7
    summ = 16

    -> i = 4
    summ = summ + arr[4] -> 16 + 9
    summ = 25

    -> i = 5 -> out of range

maxSum = summ - arr[0]
maxSum = 25 - 1
maxSum = 24

minSum = summ - arr[len(arr) - 1]
minSum = summ - arr[5 - 1] -> summ - arr[4]
minSum = 25 - 9
minSum = 16
'''