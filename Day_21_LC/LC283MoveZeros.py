def moveZeros(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)

    return nums

print(moveZeros(nums=[0, 1, 3, 12, 0]))

def moveZerosTwoPointer(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j = j + 1

    return nums

print(moveZerosTwoPointer(nums = [0, 1, 3, 12, 0]))

'''
TRACING : 

Two pointer : 

nums = [0, 1, 3, 12, 0]

j = 0
for i in range(len(nums)):
    len(nums) = 5
    -> i = 0
    if nums[i] != 0:
        nums[0] != 0 -> False

    -> i = 1
    if nums[i] != 0:
        nums[1] != 0 -> 1 != 0 => True
        nums[i], nums[j] = nums[j], nums[i]
        nums[1] = nums[0] 
        nums[0] = nums[1]

        => nums = [1, 0, 3, 12, 0]

        j = j + 1 -> 0 + 1
        j = 1

    -> 1 = 2
    if nums[i] != 0:
        nums[2] != 0 -> 3 != 0 => True
        nums[i], nums[j] = nums[j], nums[i]
        nums[2] = nums[1]
        nums[1] = nums[2]

        nums = [1, 3, 0, 12, 0]

        j = j + 1 -> 1 + 1
        j = 2
    
    -> i = 3
    if nums[i] != 0: 
        nums[3] != 0 -> 12 != 0 -> True
        nums[i], nums[j] = nums[j], nums[i]
        nums[3] = nums[2]
        nums[2] = nums[3]

        nums = [1, 3, 12, 0, 0]

        j = j + 1 -> 2 + 1
        j = 3

    -> i = 4
    if nums[i] != 0:
        nums[4] != 0 -> False

    -> i = 5 -> Out of range

    return nums

    Output = [1, 3, 12, 0, 0]
            
'''