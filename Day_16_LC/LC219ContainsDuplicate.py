def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    numSort = sorted(nums)
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if numSort[i] == numSort[j]:
                if abs(i - j) <= k:          
                    return True
                else:
                    return False
            else:
                continue
            
nums = [1, 0, 1, 1]
k = 1
result = containsNearbyDuplicate(nums, k)
print(result)