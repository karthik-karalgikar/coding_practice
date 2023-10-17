'''
QUESTION:
Check if an Array is Sorted
Problem Statement: Given an array of size n, 
write a program to check if the given array is sorted in 
(ascending / Increasing / Non-decreasing) order or not. 
If the array is sorted then return True, Else return False.
'''

#SOLUTION 1
def arrSort(arr, n):
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False
    return True

arr = [2, 4, 6, 8, 10, 13]
n = 6
res = arrSort(arr, n)
print(res)

'''
TRACING
arr = 2, 4, 6, 8, 10, 13
n = 6
i = 0, j = 1
arr[1] < arr[0] -> 4 < 2 -> False

arr = 13, 10, 8, 6, 4, 2
n = 6
i = 0, j = 1
arr[1] < arr[0] -> 10 < 13 -> True
arr[2] < arr[0] -> 
'''

#SOLUTION 2
def arrSort(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True

arr = [2, 4, 6, 8, 10, 13]
n = 6
res = arrSort(arr, n)
print(res)
