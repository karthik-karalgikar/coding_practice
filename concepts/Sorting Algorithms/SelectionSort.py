def selectionSort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums

print(selectionSort(nums=[3, 2, 1, 4]))

'''
TRACING - 

nums = [3, 2, 1, 4]

-> i = 0
    min_index = i
    min_index = 0

    -> j = 1(i + 1), until len(nums)= 4
        if nums[j] < nums[min_index]:
        nums[1] < nums[0] -> 2 < 3 -> true
            min_index = j 
            min_index = 1

    -> j = 2
        if nums[j] < nums[min_index]:
        nums[2] < nums[1] -> 1 < 2 -> true
            min_index = j
            min_index = 2

    -> j = 3
        if nums[j] < nums[min_index]:
        nums[3] < nums[2] -> 4 < 1 -> false

    nums[i], nums[min_index] = nums[min_index], nums[i]
    nums[0], nums[2] = nums[0], nums[2]

    nums = [1, 2, 3, 4]

-> i = 1
    min_index = 1

    -> j = 2
        if nums[j] < nums[min_index]:
        nums[2] < nums[1] -> 3 < 2 -> false

    -> j = 3
        if nums[j] < nums[min_index]:
        nums[3] < nums[1] -> 4 < 2 -> false

    nums[i], nums[min_index] = nums[min_index], nums[i]
    nums[1], nums[1] = nums[1], nums[1]

    nums = [1, 2, 3, 4]

-> i = 2
    min_index = 2

    -> j = 3
        if nums[j] < nums[min_index]:
        nums[3] < nums[2] -> 4 < 3 -> false

    nums[i], nums[min_index] = nums[min_index], nums[i]
    nums[2], nums[2] = nums[2], nums[2]

    nums = [1, 2, 3, 4]

-> i = 3
    min_index = 3

    -> j = 4, does not go inside loop

    nums[i], nums[min_index] = nums[min_index], nums[i]
    nums[3], nums[3] = nums[3], nums[3]

    nums = [1, 2, 3, 4]
'''