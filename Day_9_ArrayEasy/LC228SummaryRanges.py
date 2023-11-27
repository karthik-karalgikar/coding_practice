'''
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers 
in the array exactly. That is, each element of nums is covered 
by exactly one of the ranges, and there is no integer x such that
 x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

'''

def summaryRanges(nums):
    temp = []
    i = 0
    while i < len(nums):
        begin = nums[i]
        while i < len(nums) - 1 and nums[i] + 1  == nums[i + 1]: 
            i = i + 1
        end = nums[i]

        if begin == end:
            temp.append(str(begin))
        else:
            temp.append(str(begin) + "->" + str(end))
        i = i + 1
    return temp

nums = [0,1,2,4,5,7]
result = summaryRanges(nums)
print(result)

'''
TRACING:
nums = [0,1,2,4,5,7]
temp = []
i = 0
while loop:
    i < len(nums) => 0 < 6 -> true
    begin = nums[i] -> begin = 1
    while loop:
        0 < 5 and nums[0] + 1 == nums[0 + 1] 
        true and 0 + 1 == nums[1] -> 1 == 1 -> true
        i = i + 1 -> i = 1

        1 < 5 and nums[1] + 1 == nums[1 + 1]
        true and 1 + 1 == 2 -> 2 == 2 -> true
        i = i + 1 => 1 = 2

        2 < 5 and nums[2] + 1 == nums[2 + 1]
        true and 3 == 4 -> false
        true and false = false

    end = nums[2] -> end = 2

    if begin == end -> false
    else:
        temp.append(str(0) -> str(2))
        => temp = ["0" -> "2"]
    
    i = 2 + 1 -> i = 3

3 < 6 -> true
    begin = nums[3] -> begin = 4
    while loop:
        3 < 5 and nums[3] + 1 == nums[3 + 1]
        true and 4 + 1 == nums[4]
        true and 5 == 5 -> true
        i = i + 1 -> i = 4

        4 < 5 and nums[4] + 1 == nums[4 + 1]
        true and 5 + 1 == nums[5]
        true and 6 == 7 -> false

    end = nums[4] -> end = 5

    if begin == end -> false
    else:
        temp.append(str(4) -> str(5))
        => temp = ["0" -> "2", "4" -> "5"]

    i = 4 + 1 -> i = 5

5 < 6 -> true
    begin = nums[5] -> begin = 7
    while loop:
        5 < 5 -> false, no need to check the other condition
    emd = nums[5] -> end = 7

    if begin == end:
        temp.append(str(7))

return temp 

temp = ["0" -> "2", "4" -> "5", "7"] 


'''