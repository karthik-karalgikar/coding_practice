def InsertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key

    return nums

print(InsertionSort(nums=[3, 1, 2, 4]))

'''
nums = [3, 1, 2, 4]

-> i = 1
    key = nums[i] -> nums[1]
    key = 1
    
    j = i - 1
    j = 0

    while j >= 0 and nums[j] > key:
    j >= 0 -> true
    nums[0] > 1 -> 3 > 1 -> true 

        nums[j + 1] = nums[j]
        nums[1] = nums[0]
        nums[1] = 3
        j = j - 1
        j = -1

        nums = [3, 3, 2, 4]
    
    nums[j + 1] = key
    nums[0] = 1

    nums = [1, 3, 2, 4]

-> i = 2
    key = nums[i] -> nums[2]
    key = 2
    
    j = i - 1
    j = 1

    while j >=0 and nums[j] > key:
    j = 1 -> true
    nums[1] > 2 -> 3 > 2 -> true

        nums[j + 1] = nums[j]
        nums[2] = nums[1]
        nums[2] = 3

        j = j - 1
        j = 0

        nums = [1, 3, 3, 4]

    j = 0 -> true
    nums[0] > key -> 0 > 2 -> false

    nums[j + 1] = key
    nums[1] = 2

    nums = [1, 2, 3, 4]

-> i = 3
    key = nums[i] = nums[3]
    key = 4

    j = i - 1
    j = 2

    while j >= 0 and nums[j] > key:
    j = 2 >= 0 -> true
    nums[2] > 4 -> 3 > 4 -> false

    nums[j + 1] = key
    nums[3] = 4 -> already there

return nums
nums = [1, 2, 3, 4]

'''