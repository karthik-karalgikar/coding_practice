# from unittest import result


def removeDuplicates(nums):
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i = i + 1
    
    return len(nums)

nums = [1,1,2,2,4,5]
res = removeDuplicates(nums)
print(res)

# '''
# TRACING:
# nums = [1,1,2,2,4,5]
# i = 1
# while i < len(nums):
#     => 1 < 6 -> true
#     nums[1] == nums[0] => 1 == 1
#     true
#     pop(1)
#     => nums = [1,2,2,4,5]

#     => 1 < 5 -> true
#     nums[1] == nums[0] => 2 == 1
#     false
#     i = i + 1 -> i = 2

#     => 2 < 5 -> true
#     nums[2] == nums[1] => 2 == 2
#     true
#     pop(2)
#     => nums = [1,2,4,5]

#     => 2 < 4 -> true
#     nums[2] == nums[1] => 4 == 2
#     false
#     i = i + 1 -> i = 3

#     => 3 < 4 -> true
#     nums[3] == nums[2] => 5 == 4
#     false
#     i = i + 1 -> i = 4

#     => 4 < 4 -> false
#  comes out of while loop
#  returns length of nums, i.e., 4

#  OUTPUT = 4

# '''

def removeDuplicates(nums):
		a = set(nums)
        
		return len(a)

nums = [1,1,2,2,4,5]
res = removeDuplicates(nums)
print(res)

#commment