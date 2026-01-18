def maximumDifference(nums):
    max_diff = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if i < j and nums[i] < nums[j]:
                diff = nums[j] - nums[i]
                max_diff = max(max_diff, diff)
        
    if max_diff == 0:
        return -1
    
    return max_diff

nums = [7,1,5,3,6,4]
print(maximumDifference(nums))

'''
TRACING : 

nums = [7, 1, 5, 4]
max_diff = 0

for i in range(len(nums)):
    -> i = 0, len(nums) = 4
    for j in range(i + 1, len(nums)):
        -> j = 1, len(nums) = 4

        if i < j and nums[i] < nums[j]:
            0 < 1 -> true 
            nums[i] = nums[0] = 7
            nums[j] = nums[1] = 1
            7 < 1 -> false

        -> j = 2, len(nums) = 4

        if i < j and nums[i] < nums[j]:
            0 < 2 -> true
            nums[i] = nums[0] = 7
            nums[j] = nums[2] = 5
            7 < 5 -> false

        -> j = 3, len(nums) = 4

        if i < j and nums[i] < nums[j]:
            0 < 3 -> true
            nums[i] = nums[0] = 7
            nums[j] = nums[3] = 4
            7 < 4 -> false

        -> j =  4, len(nums) = 4 -> out of range

    -> i = 1, len(nums) = 4
    for j in range(i + 1, len(nums)):
        -> j = 2, len(nums) = 4

        if i < j and nums[i] < nums[j]:
            1 < 2 -> true
            nums[i] = nums[1] = 1
            nums[j] = nums[2] = 5
            1 < 5 -> true
            diff = nums[j] - nums[i]
            diff = 5 - 1
            diff = 4
            max_diff = max(max_diff, diff) -> max(0, 4)
            max_diff = 4

        -> j = 3, len(nums) = 4

        if i < j and nums[i] < nums[j]:
            1 < 3 -> true
            nums[i] = nums[1] = 1
            nums[j] = nums[3] = 4
            1 < 4 -> true
            diff = nums[j] - nums[i]
            diff = 4 - 1
            diff = 3
            max_diff = max(max_diff, diff) -> max(4, 3)
            max_diff = 4

        -> j = 4, len(nums) = 4 -> out of range

    -> i = 2, len(nums) = 4
    for j in range(i + 1, len(nums)):
        -> j = 3, len(nums) = 4

        if i < j and nums[i] < nums[j]:
            2 < 3 -> true
            nums[i] = nums[2] = 5
            nums[j] = nums[3] = 4
            5 < 4 -> false

        -> j = 4, len(nums) = 4 -> out of range

    -> i = 3, len(nums) = 4
    for j in range(i + 1, len(nums)):
        -> j = 4, len(nums) = 4 -> out of range

    -> i = 4, len(nums) = 4 -> out of range

if max_diff == 0:
    false

return max_diff -> 4

Output = 4

'''