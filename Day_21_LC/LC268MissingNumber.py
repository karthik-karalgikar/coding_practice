def missingNumber(nums):
    nums.sort()
    for i in range(len(nums) + 1):
        if i not in nums:
            return i
        
print(missingNumber(nums=[3,0,1]))

'''
TRACING : 

nums = [3, 0, 1]

nums.sort() -> [0, 1, 3]

for i in range(len(nums) + 1):
    -> i = 0:
    if i not in nums:
        0 not in nums -> false
    
    -> i = 1
    if i not in nums:
        1 not in nums -> false

    -> i = 2
    if i not in nums:
        2 not in nums -> true

        return i

    Output = 2
'''

def missingNumberSum(nums):
    n = len(nums)
    summ = n * (n + 1) // 2
    numsSum = sum(nums)

    return summ - numsSum

print(missingNumberSum(nums = [0, 1, 3, 4]))