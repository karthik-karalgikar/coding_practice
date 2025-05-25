'''
Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.
'''

def removeElement(nums, val):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index = index + 1

    return index

nums = [3,2,2,3]
val = 3
result = removeElement(nums, val)
print(result)


'''
TRACING

nums = [3,2,2,3]
val = 3

index = 0
for loop:
    i = 0
    nums[0] = 3 != 3 -> false

    i = 1
    nums[1] = 2 != 3 -> true
    nums[index] = nums[i], i.e., nums[0] = 2
    nums = [2,2,2,3]
    index = 1

    i = 2
    nums[2] = 2 != 3 -> true
    nums[index] = nums[i], i.e., nums[1] = 2
    nums = [2,2,2,3]
    index = 2

    i = 3
    nums[3] = 3 != 3 -> false

comes out of for loop
returns the value of index, that is, 2

'''