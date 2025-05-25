'''
LEETCODE 1752
Given an array nums, return true if the array was originally sorted 
in non-decreasing order, then rotated some number of positions (including zero). 
Otherwise, return false.
'''

def check(nums):
    temp = nums[:]
    temp.sort()
    for i in range(len(nums)):
        temp = [temp[-1]] + temp[:-1]  
        if temp == nums:
            return "true"

    return "false"

nums = [2,2,3,4]
result = check(nums)
print(result)

'''
TRACING:

TESTCASE 1

nums = [3,4,5,1,2]
2 -> initializing another variable named temp and storing the contents of nums
     in temp. 
     => temp = [3,4,5,1,2]
NOTE: if you want to copy the contents of any list into another list, then 
use slicing. if you use temp = nums, and when you update temp, nums will also 
be updated. but if you use slicing only temp will be updated. 

3 -> sort the temp list
  => temp = [1,2,3,4,5]

for loop: will run from 0 to length of nums
    i = 0
    temp[-1] -> 5 and temp[:-1] is all the elements up to the last element
    (last element not included)
    and then concatenate these two to form temp
    => temp = [5,1,2,3,4]
    check whether this is equal to nums. 
    it is not
    
    i = 1
    temp[-1] -> 4 and temp[:-1] -> 5,1,2,3
    => temp = [4,5,1,2,3]
    temp is not equal to nums

    i = 2
    temp[-1] -> 3 and temp[:-1] -> 4,5,1,2
    => temp = [3,4,5,1,2]
    temp is equal to nums
    print "true"

TESTCASE 2:
nums = [2,1,3,4]
temp.sort = [1,2,3,4]

for loop:
    i = 0
    temp[-1] = 4 => temp = [4,1,2,3]
    temp is not equal to nums

    i = 1
    temp[-1] = 3 => temp = [3,4,1,2]
    temp is nnot equal to nums

    i = 2
    temp[-1] = 2 => temp = [2,3,4,1]
    temp is not equal to nums

    i = 3
    temp[-1] = 1 => temp = [1,2,3,4]
    temp is not equal to nums

comes out of for loop
print "false"
'''