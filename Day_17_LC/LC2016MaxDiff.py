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

nums = [7,1,5,4]
print(maximumDifference(nums))