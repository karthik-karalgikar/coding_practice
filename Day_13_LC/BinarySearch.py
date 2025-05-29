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

'''
TRACING : 
nums = [1,2,3,4,5]
ele = 2

low = 0
high = len(nums) - 1 => 5 - 1 
high = 4

while loop:
    low <= high -> 2 <= 4 -> true
    goes inside 
    mid = (low + high) // 2 => (0 + 4) // 2 -> 4 // 2
    mid = 2

    if nums[mid] == ele -> nums[2] == 2
    nums[2] = 3
    3 == 2 -> false
    
    moves on to next condition

    elif nums[mid] < ele:
        nums[2] < 2 -> 3 < 2 -> false

    moves on to next condition

    else: 
        high = mid - 1 => 2 - 1 
        high = 1

    low = 0
    high = 1
    mid = 2

    while low <= high -> 0 <= 1 -> true
    goes inside

    mid = (low + high) // 2 => (0 + 1) // 2 -> 1 // 2
    mid = 0

    low = 0
    high = 1
    mid = 0

    nums[0] == ele -> 1 == 2 -> false

    next condition

    elif nums[mid] < ele:
        nums[0] < 2 -> 1 < 2 => true
        low = mid + 1
        low = 0 + 1 
        low = 1

    low = 1
    high = 1
    mid = 0

    while low <= high -> 1 <= 1 -> true
    goes inside

    mid = (low + high) // 2 -> (1 + 1) // 2
    mid = 1

    low = 1
    high = 1
    mid = 1

    nums[mid] == ele:
    nums[1] == 2 -> 2 == 2 -> true

    return mid -> return 1

'''