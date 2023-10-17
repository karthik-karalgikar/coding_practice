'''
QUESTION :
Find the Largest element in an array
Problem Statement: Given an array, we have to find the largest element 
in the array.
'''

#SOLUTION 1

def large(arr):
    arr.sort
    return arr[-1]

arr = list(map(int, input().split()))
result = large(arr)
print(result)

'''
TRACING 
arr = 3 4 1 0 29 12 99
arr.sort = 0 1 3 4 12 29 99
arr[-1] = 99
99 is printed as it is the largest
'''

#SOLUTION 2

def large(arr, n):
    max = arr[0]
    for i in range(0, n):
        if max < arr[i]:
            max = arr[i]
    return max

n = int(input())
arr = list(map(int, input().split()))
result = large(arr, n)
print(result)

'''
TRACING
n = 5
arr = 4 3 10 99 2
max = 4
i = 0
max < arr[0] -> 4 < 4 -> no
i = 1
max < arr[1] -> 4 < 3 -> no
i = 2
max < arr[2] -> 4 < 10 -> yes
max = 10
i = 3
max < arr[3] -> 10 < 99 -> yes
max = 99
i = 4
max < arr[4] -> 99 < 2 -> no
exit loop
return 99 as the largest number

'''
