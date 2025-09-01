def bubblesort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

print(bubblesort(nums=[3,2,1,4]))

'''
TRACING - 
nums = [3, 2, 1, 4]

for loop 
    -> i = 0
        -> j = 0, until (4 - 0 - 1) = 3
        nums[j] > nums[j + 1]
        nums[0] > nums[1] -> 3 > 2 -> true
        swap
        nums = [2, 3, 1, 4]
        
        -> j = 1
        nums[j] > nums[j + 1]
        nums[1] > nums[2] -> 3 > 1 -> true
        swap
        nums = [2, 1, 3, 4]


        -> j = 2
        nums[j] > nums[j + 1]
        nums[2] > nums[3] -> 3 > 4 -> false
        
        nums = [2, 1, 3, 4]

    -> i = 1
        -> j = 0, until (4 - 1 - 1) = 2
        nums[j] > nums[j + 1]
        nums[0] > nums[1] -> 1 > 2 -> false
        nums = [1, 2, 3, 4]

        -> j = 1
        nums[j] > nums[j + 1]
        nums[1] > nums[2] -> 2 > 3 -> false
        nums = [1, 2, 3, 4]

    -> i = 2
        -> j = 0, until (4 - 2 - 1) = 1
        nums[j] > nums[j + 1]
        nums[0] > nums[1] -> 1 > 2 -> false
        nums = [1, 2, 3, 4]

    -> i = 3
        -> j = 0, until (4 - 3 - 1) = 0
        does not go inside j loop
    
    nums = [1, 2, 3, 4]
'''
