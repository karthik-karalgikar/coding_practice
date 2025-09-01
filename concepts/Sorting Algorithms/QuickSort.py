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