def smallestMissingPositive(nums):
    n = len(nums)

    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]


    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
        
    return n + 1

print(smallestMissingPositive(nums=[3, 4, -1, 1]))

'''
TRACING : 

nums = [3, 4, -1, 1]

n = len(nums) 
n = 4

for i in range(n):
    -> i = 0
    while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
    -> 1 <= nums[i] <= n
    -> 1 <= nums[0] <= 4 -> 1 <= 3 <= 4 -> True
    
    -> nums[nums[0] - 1] != nums[0]
    -> nums[3 - 1] != 3 => nums[2] != 3 -> -1 != 3 -> True

        swap -> 
        nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        nums[2], nums[0] = nums[0], nums[2]

        nums = [-1, 4, 3, 1]

    -> i = 0(while loop runs until it is false)
    while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
    -> 1 <= nums[i] <= n 
    -> 1 <= nums[0] <= 4 -> 1 <= -1 <= 4 -> False



    -> i = 1
    while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]
    -> 1 <= nums[1] <= 4
    -> 1 <= 4 <= 4 -> True

    -> nums[nums[i] - 1] != nums[i]
    -> nums[nums[1] - 1] != nums[1] -> nums[3] != nums[1] -> 1 != 4 -> True

        swap -> 
        nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        nums[3], nums[1] - nums[1], nums[3]

        nums = [-1, 1, 3, 4]

    -> i = 1(running until while loop is false)
    while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]
    -> 1 <= nums[1] <= 4
    -> 1 <= 1 <= 4 -> True

    -> nums[nums[i] - 1] != nums[i]
    -> nums[nums[1] - 1] != nums[1] -> nums[0] != nums[1] -> -1 != 1 -> True

        swap -> 
        nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        nums[0], nums[1] = nums[1], nums[0]

        nums = [1, -1, 3, 4]

    -> i = 1
    while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]
    -> 1 <= nums[1] <= n 
    -> 1 <= -1 <= 4 -> False

    nums = [1, -1, 3, 4]

    -> i = 2
    while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]
    -> 1 <= nums[2] <= n
    -> 1 <= 3 <= 4 -> True

    nums[nums[i] - 1] != nums[i]
    -> nums[nums[2] - 1] != nums[2]
    -> nums[2] != nums[2] -> False

    -> i = 3
    while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]
    -> 1 <= nums[3] <= 4
    -> 1 <= 4 <= 4 -> True

    nums[nums[i] - 1] != nums[i]
    -> nums[nums[3] - 1] != nums[3]
    -> nums[3] != nums[3] -> False

    i = 4 -> Out of range

nums = [1, -1, 3, 4]

for i in range(n):
    -> i = 0
    if nums[i] != i + 1:
    -> nums[0] != 0 + 1
    -> 1 != 1 -> false

    -> i = 1
    if nums[i] != i + 1:
    -> nums[1] != 1 + 1
    -> -1 != 2:
        return i + 1

Output = 2


    



'''