def searchinsert(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low

print(searchinsert(nums=[1,3,5,6], target=5))

'''
TRACING  :

nums = [1,3,5,6]
target = 5

low = 0
high = len(nums) - 1 -> 4 - 1
high = 3

while low <= high:
    0 <= 3 -> true
    mid = (low + high) // 2
    mid = (0 + 3) // 2
    mid = 1

    if nums[mid] == target:
        nums[1] == 5
        3 == 5 -> false

    elif nums[mid] < target:
        3 < 5 -> true
        low = mid + 1
        low = 2

    2 <= 3 -> true
    mid = (low + high) // 2
    mid = 2 + 3 // 2
    mid = 2

    if nums[mid] == target:
        nums[2] == target:
        5 == 5 -> true
        return mid

Output = 2

'''

'''
TRACING 2:

nums = [1, 3, 5, 6]
target = 2

low = 0
high = 3

while low <= high:
    0 <= 3 -> true
    mid = (low + high) // 2
    mid = 1

    if nums[mid] == target:
        3 == 5 -> false

    elif nums[mid] < target:
        3 < 2 -> false

    else:
        high = mid - 1
        high = 0

    0 <= 0 -> true
    mid = 0 + 0 // 2
    mid = 0

    if nums[mid] == target:
        1 == 2 -> false

    elif nums[mid] < target:
        1 < 2 -> true
        low = mid + 1
        low = 1

    1 <= 0: -> false

return low

low = 1

Output = 1
'''