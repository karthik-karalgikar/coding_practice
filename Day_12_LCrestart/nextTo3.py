'''
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
'''

def nexttoThree(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums = [1, 2, 3, 5, 4]
res = nexttoThree(nums)
print(res)