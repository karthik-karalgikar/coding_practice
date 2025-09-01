def QuickSort(nums):
    if len(nums) <= 1:
        return nums
    
    pivot = nums[0]
    left = []
    right = []

    for i in range(1, len(nums)):
        if nums[i] <= pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])

    return QuickSort(left) + [pivot] + QuickSort(right)

print(QuickSort(nums=[3, 1, 2, 4]))

'''
TRACING - 

nums = [3, 1, 2, 4]

pivot = nums[0]
pivot = 3
left = []
right = []

for i in range(1, len(nums)):
    -> i = 1
    if nums[i] <= pivot:
    -> nums[1] <= 3 -> 1 <=3 -> true
        left.append(nums[i]) -> nums[1]
        left = [1]

    -> i = 2
    if nums[i] <= pivot:
    -> nums[2] <= 3 -> 2 <= 3-> true
        left.append(nums[i]) -> nums[2]
        left = [1, 2]

    -> i = 3
    if nums[i] <= pivot:
    -> nums[3] <= 3 -> 4 <= 3 <= false

    else:
        right.append(nums[i]) -> nums[3]
        right = [4]

        left = [1, 2]
        right = [4]
        pivot = 3

        return QuickSort(left)

'''