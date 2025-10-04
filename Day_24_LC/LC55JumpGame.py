def canJump(nums):
    if len(nums) == 1:
        return True
    j = 0
    for i in range(len(nums)):
        j = i + nums[i]
        if j == len(nums) - 1:
            return True
        i = nums[i]

    return False

print(canJump(nums=[2, 3, 1, 1, 4]))

        