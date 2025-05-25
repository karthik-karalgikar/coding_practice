def longest_cont_subarray(nums):
    n = len(nums)
    luffy = [1] * n
        
    for i in range(1, n):
        if nums[i] > nums[i-1]:
            luffy[i] = luffy[i-1] + luffy[i]
        
    return max(luffy)

nums = [1, 3, 4, 2, 3, 4, 5]
print(longest_cont_subarray(nums))

'''
TRACING:
nums = [1,2,4,2,3,4,5]
n = 7
luffy = [1,1,1,1,1,1,1]
for loop:
    i = 1
    nums[1] > nums[0] => 2 > 1 -> true
    luffy[1] = luffy[0] + luffy[1] => 1 + 1 => 2
    luffy = [1,2,1,1,1,1,1]

    i = 2
    nums[2] > nums[1] => 4 > 2 -> true
    luffy[2] = luffy[1] + luffy[2] => 2 + 1 => 3
    luffy = [1,2,3,1,1,1,1]

    i = 3
    nums[3] > nums[2] => 2 > 4 -> false
    luffy = [1,2,3,1,1,1,1]

    i = 4
    nums[4] > nums[3] => 3 > 2 -> true
    luffy[4] = luffy[3] + luffy[4] => 1 + 1 => 2
    luffy = [1,2,3,1,2,1,1]

    i = 5
    nums[5] > nums[4] => 4 > 3 -> true
    luffy[5] = luffy[4] + luffy[5] => 2 + 1 => 3
    luffy = [1,2,3,1,2,3,1]

    i = 6
    nums[6] > nums[5] => 5 > 4 -> true
    luffy[6] = luffy[5] + luffy[6] => 3 + 1 => 4
    luffy = [1,2,3,1,2,3,4]

max(luffy) = 4
'''

