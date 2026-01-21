'''
LEETCODE 189
Given an integer array nums, 
rotate the array to the right by k steps, where k is non-negative.
'''

def rotate(nums, k):

    k = k % len(nums)
    
    nums[:] = nums[-k:] + nums[:-k]

    return nums

k = 7
nums = [1, 2]
result = rotate(nums, k)
print(result)

'''
TRACING

k = 7
k = k % len(nums)
k = 7 % 2
k = 1

using slicing, 
nums[-k:] means that nums is being updated by taking all the elements starting
from -k to the end, that is, 
[1,2,3,4,5,6,7] and k = 3, so this implies
nums[-3 to end], that is, 
the last element is always -1, i.e.,
7 = -1, 6 = -2, 5 = -3
so the nums is updated to [5,6,7]

for nums[:-k], means that nums is being updated by taking all the elements 
starting from 0th index to -kth index
=> 0th index to -3rd index
[1, 2, 3, 4]

and this is being added to the present list. 
so nums becomes => [5,6,7,1,2,3,4]
which is the expected output
'''
