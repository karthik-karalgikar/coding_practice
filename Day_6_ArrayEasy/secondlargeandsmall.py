'''
QUESTION: 
Find Second Smallest and Second Largest Element in an array
Problem Statement: Given an array, find the second smallest and 
second largest element in the array. 
Print ‘-1’ in the event that either of them doesn’t exist.
'''

#SOLUTION 1

def seclargeandsmall(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)
    arr.sort()
    small = arr[1]
    large = arr[n - 2]
    return small, large

arr = [1, 5, 0, 2, 45, 69, 22]
n = 7
result = seclargeandsmall(arr, n)
print(result)

'''TRACING
given array and n: 
[1, 5, 0, 2, 45, 69, 22], 7
sort the array:
0, 1, 2, 5, 22, 45, 69
arr[1] = 1 -> small = 1
arr[7-2] = arr[5] = 45 -> large = 45
return 1 and 45
'''

#SOLUTION 2

def secondSmallest(arr, n):
    if (n < 2):
        return -1
    small = float('inf')
    second_small = float('inf')
    for i in range(n):
        if (arr[i] < small):
            second_small = small
            small = arr[i]
        elif (arr[i] < second_small and arr[i] != small):
            second_small = arr[i]
    return second_small

def secondLargest(arr, n):
    if (n < 2):
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    return second_large

arr = [1, 2, 4, 7, 7, 5]
n = len(arr)
sS = secondSmallest(arr, n)
sL = secondLargest(arr, n)
print(sS)
print(sL)