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

'''
MAXIMUM SUM OF CONTIGIOUS SUBARRAY:

nums = [1, -2, 3, 4, -5, 8]
len(nums) = 6

max_so_far = nums[0]
max_so_far = 1

max_ending_here = nums[0]
max_ending_here = 1

for i in range(1, len(nums)):
    -> i = 1
    max_ending_here = max_ending_here + nums[i]
    max_ending_here = 1 + nums[1] -> 1 + -2
    max_ending_here = -1

    if max_ending_here < 0: -> true
        max_ending_here = 0

    if max_so_far < max_ending_here:
    -> 1 < 0 -> false

    -> i = 2
    max_ending_here = max_ending_here + nums[i]
    max_ending_here = 0 + nums[2] -> 0 + 3
    max_ending_here = 3

    if max_ending_here < 0: -> false

    if max_so_far < max_ending_here:
    -> 1 < 3 -> true
        max_so_far = max_ending_here
        max_so_far = 3

    -> i = 3
    max_ending_here = max_ending_here + nums[i]
    max_ending_here = 3 + nums[3] -> 3 + 4
    max_ending_here = 7

    if max_ending_here < 0: -> false

    if max_so_far < max_ending_here: 
    -> 3 < 7 -> true
        max_so_far = max_ending_here
        max_so_far = 7

    -> i = 4
    max_ending_here = max_ending_here + nums[i]
    max_ending_here = 7 + nums[4] -> 7 + -5 
    max_ending_here = 2

    if max_ending_here < 0: -> false

    if max_so_far < max_ending_here:
    -> 7 < 2 -> false

    -> i = 5
    max_ending_here = max_ending_here + nums[i]
    max_ending_here = 2 + nums[5] -> 2 + 8
    max_ending_here = 10

    if max_ending_here < 0 -> false

    if max_so_far < max_ending_here:
    -> 7 < 10 -> true
        max_so_far = max_ending_here
        max_so_far = 10

    
Output = 10

    
'''