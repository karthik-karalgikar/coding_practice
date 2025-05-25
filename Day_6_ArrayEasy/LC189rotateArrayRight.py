'''
LEETCODE 189
Given an integer array nums, 
rotate the array to the right by k steps, where k is non-negative.
'''

def rotate(nums, k):
    
    nums[:] = nums[-k:] + nums[:-k]

    return nums

k = 3
nums = [1, 2, 3, 4, 5, 6, 7]
result = rotate(nums, k)
print(result)

'''
TRACING

using slicing, 
nums[-k:] means that nums is being updated by taking all the elements starting
forom -k to the end, that is, 
[1,2,3,4,5,6,7] and k = 3, so this implies
nums[-3 to end], that is, 
the last element is always -1, i.e.,
7 = -1, 6 = -2, 5 = -3
so the nums is updated to [5,6,7]

for nums[:-k], means that nums is being updated by taking all the elements 
starting from 0th index to -kth index
=> 0th index to -3rd index
[1, 2, 3, 4]

and this is being concatenated. 
so nums becomes => [5,6,7,1,2,3,4]
which is the expected output
'''
