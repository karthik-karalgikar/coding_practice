def max_subarray(nums):
    max_so_far = nums[0]
    max_ending_here = nums[0]

    start = 0
    end = 0
    temp = 0

    for i in range(1, len(nums)):
        if max_ending_here + nums[i] < nums[i]:
            max_ending_here = nums[i]
            temp = i
        else:
            max_ending_here = max_ending_here + nums[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp
            end = i

    return nums[start:end + 1]

nums = [1, -2, 3, 4, -5, 8]
print(max_subarray(nums))

'''
TRACING - 

nums = [1, -2, 3, 4, -5, 8]

max_so_far = nums[0]
max_so_far = 1

max_ending_here = nums[0]
max_ending_here = 1

start = 0
end = 0
temp = 0

for i in range(1, len(nums)):
    -> i = 1
    if max_ending_here + nums[i] < nums[i]:
    -> 1 + nums[1] < nums[1] -> 1 + -2 = -1 < -2 -> false

    else:   
        max_ending_here = max_ending_here + nums[i]
        max_ending_here = 1 + nums[1] -> 1 + -2
        max_ending_here = -1

    if max_ending_here > max_so_far:
    -> -1 > 1 -> false

    max_ending_here = -1
    max_so_far = 1
    start = 0
    end = 0
    temp = 0

    -> i = 2
    if max_ending_here + nums[i] < nums[i]:
    -> -1 + nums[2] < nums[2] -> -1 + 3 < 3 -> true
        max_ending_here = nums[i] -> nums[2]
        max_ending_here = 3
        temp = i
        temp = 2

    if max_ending_here > max_so_far:
    -> 3 > 1 -> true
        max_so_far = max_ending_here
        max_so_far = 3
        start = temp
        start = 2
        end = i
        end = 2

    max_ending_here = 3
    max_so_far = 3
    start = 2
    end = 2
    temp = 2

    -> i = 3
    if max_ending_here + nums[i] < nums[i]:
    -> 3 + nums[3] < nums[3] -> 3 + 4 < 3 -> false
    
    else:
        max_ending_here = max_ending_here + nums[i]
        max_ending_here = 3 + nums[3] -> 3 + 4 
        max_ending_here = 7

    if max_ending_here > max_so_far:
    -> 7 > 3 -> true
        max_so_far = max_ending_here
        max_so_far = 7
        start = temp
        start = 2
        end = i
        end = 3

    max_ending_here = 7
    max_so_far = 7
    start = 2
    end = 3
    temp = 2

    -> i = 4
    if max_ending_here + nums[i] < nums[i]:
    -> 7 + nums[4] < nums[4] -> 7 + -5 < -5 -> false
    
    else:
        max_ending_here = max_ending_here + nums[i]
        max_ending_here = 7 + -5
        max_ending_here = 2

    if max_ending_here > max_so_far :
    -> 2 > 4 -> false

    max_ending_here = 2
    max_so_far = 7
    start = 2
    end = 3
    temp = 2    

    -> i = 5
    if max_ending_here + nums[i] < nums[i]:
    -> 2 + nums[5] < nums[5] -> 2 + 8 < 9 -> false
    
    else:
        max_ending_here = max_ending_here + nums[i]
        max_ending_here = 2 + 8
        max_ending_here = 10

    if max_ending_here > max_so_far : 
    -> 10 > 4 -> true
        max_so_far = max_ending_here
        max_so_far = 8
        start = temp 
        start = 4
        end = i
        end = 5

max_ending_here = 10
max_so_far = 10
start = 2
end = 5
temp = 2

return nums[start:end + 1]
nums[2 : 5 + 1] -> nums[2 : 7]

Output = [3, 4, -5, 8]

'''

