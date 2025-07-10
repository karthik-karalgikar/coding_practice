def kedaneAlgo(nums):
    max_so_far = nums[0]
    max_ending_here = nums[0]

    for i in range(1, len(nums)):
        max_ending_here = max_ending_here + nums[i]

        if max_ending_here < 0:
            max_ending_here = 0

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    
    return max_so_far

nums = [1, -2, 3, 4, -5, 8]
print(kedaneAlgo(nums))