def topKFrequent(nums, k):
    
    dup = []
    numSort = sorted(nums)

    if len(nums) == k:
        return nums
                
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] in dup:
                continue

            if i == j:
                continue

            if numSort[i] == numSort[j]:
                dup.append(numSort[i])

                if len(dup) == k:
                    return dup
                break

    return dup

nums = [5,3,1,1,1,3,73,1]
k = 2
result = topKFrequent(nums, k)
print(result)