def indexOfDuplicate(nums, target):
    low = 0
    high = len(nums) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            result = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

print(indexOfDuplicate(nums=[1, 2, 3, 4, 5], target= 3))

'''
TRACING : 

Same as Binary Search, but this checks other elements also and then updates the value of result if it does find any other
element.
'''