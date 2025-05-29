def binarySearch(nums, ele):

    low = 0
    high = len(nums) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == ele:
            return mid
        elif nums[mid] < ele:
            low = mid + 1
        else:
            high = mid - 1
    
    return mid

nums = [1,2,3,4,5]
ele = 2
result = binarySearch(nums, ele)
print(result)