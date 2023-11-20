def max_chakra_sum(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    max_sum = [0] * n
    max_sum[0] = nums[0]
    max_sum[1] = max(nums[0], nums[1])
    for i in range(2, n):
        max_sum[i] = max(max_sum[i - 1] ,max_sum[i - 2] + nums[i])

    return max_sum[-1]

n = 5
nums = [1,2,3,4,5]
result = max_chakra_sum(nums)
print(result) 

'''
TRACING:
nums = [1,2,3,4,5]
n != 0
n != 1
max_sum = [0,0,0,0,0]
max_sum[0] = nums[0] => max_sum = [1,0,0,0,0]
max_sum[1] = max(nums[0], nums[1])
=> max(1, 2) -> 2
=> max_sum  = [1,2,0,0,0]
for loop:
    i = 2
    max_sum[2] = max(max_sum[2-1], max_sum[2-2] + nums[2])
    max_sum[2] = max(max_sum[1], max_sum[0] + nums[2])
    max_sum[2] = max(2, 1 + 3) -> max(2, 4)
    max_sum[2] = 4
    max_sum = [1,2,4,0,0]

    i = 3
    max_sum[3] = max(max_sum[3-1], max_sum[3-2] + nums[3])
    max_sum[3] = max(4, 2 + 4) -> max(4, 6)
    max_sum[3] = 6
    max_sum = [1,2,4,6,0]

    i = 4
    max_sum[4] = max(max_sum[4-1], max_sum[4-2] + nums[4])
    max_sum[4] = max(6, 4 + 5) -> max(6, 9)
    max_sum[4] = 9
    max_sum = [1,2,4,6,9]

max_sum[-1] = 9
'''