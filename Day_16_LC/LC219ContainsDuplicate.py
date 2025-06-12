def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    # seen = []
    # numSort = sorted(nums)
    # for i in range(len(nums)):
    #     for j in range(1, len(nums)):
    #         if numSort[i] == numSort[j]:
    #             if abs(i - j) <= k:          
    #                 return True
    #             else:
    #                 seen.append(i)
    #         else:
    #             continue

    seen = {}

    for i, val in enumerate(nums):
        if val in seen and i - seen[val] <= k:
            return True
        else:
            seen[val] = i

    return False
            
nums = [1, 0, 1, 1]
k = 1
result = containsNearbyDuplicate(nums, k)
print(result)

'''
TRACING : 

nums = [1, 0, 1, 1]
k = 1

seen = {}

for i, val in enumerate(nums):

enumerate(nums) = (0, 1) (1, 0) (2, 1) (3, 1)

for (0, 1) -> i = 0, val = 1

if val in seen -> 1 in {} -> false
else:
    seen[val] = i
    => seen[1] = 0
    => seen = {1 : 0}

for (1, 0) -> i = 1, val = 0

if val in seen -> 0 in {1 : 0} -> false
else:
    seen[val] = i
    => seen[0] = 1
    => seen = {1 : 0, 0 : 1}

for (2, 1) -> i = 2, val = 1

if val in seen -> 1 in {1 : 0, 0 : 1} -> true
and
i - seen[val] <= k 
=> 2 - seen[1] <= 1
=> 2 - 0 <= 1
=> 2 <= 1 -> false

else:
    seen[val] = i
    seen[1] = 2
    => seen = {1 : 2, 0 : 1}

for (3, 1) -> i = 3, val = 1

if val in seen -> 1 in {1 : 2, 0 : 1} -> true
and
i - seen[val] <= k
=> 3 - seen[1] <= 1
=> 3 - 2 <= 1
=> 1 <= 1 -> true

return True

Output = True

'''