#Solution 1 - Time Limit Exceeded

def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    max_average = float('-inf')

    for i in range(len(nums) - k + 1):
        summ = 0
        for j in range(i, i + k):
            summ = summ + nums[j]
        
        average = summ / float(k)
        max_average = max(max_average, average)
        
    return max_average

nums = [1, 12, -5, -6, 50, 3]
k = 4
result = findMaxAverage(nums, k)
print(result)

'''
TRACING:

nums = [1, 12, -5, -6, 50, 3]
k = 4

max_average is set to -infinity

for loop:
    range - len(nums) - k + 1 -> 6 - 4 + 1
    => 3
    so this will run 3 times. like,
    1 + 12 + (-5) + (-6)
    12 + (-5) + (-6) + 50
    -5 + (-6) + 50 + 3

    now, 
    i = 0
    summ = 0
    j = 0, range = (i + k) => 0 + 4 -> 4 (so until 3rd index)

    summ = summ + nums[j] -> summ + nums[0]
    summ = 0 + 1
    summ = 1

    j = 1, range = (i + k) => 0 + 4 -> 4 (so until 3rd index)

    summ = summ + nums[j] -> summ + nums[1]
    summ = 1 + 12
    summ = 13

    j = 2, range = 4 (until 3rd index)
    
    summ = summ + nums[j] -> summ + nums[2]
    summ = 13 + (-5)
    summ = 8

    j = 3 (last)

    summ = summ + nums[j] -> summ + nums[3]
    summ = 8 + (-6)
    summ = 2

    average = summ / float(k) 
    => 2 / 4 
    average = 0.5

    max_average = max(max_average, average)
    -> max(-infinity, 0.5)
    max_average = 0.5

    --------------------------

    i = 1
    summ = 0
    j = 1, range = (i + k) => 1 + 4 -> 5 (so until 4th index)

    summ = summ + nums[j] -> summ + nums[1]
    summ = 0 + 12
    summ = 12

    j = 2, range = (i + k) => 1 + 4 -> 5 ( until 4th index)

    summ = summ + nums[j] -> summ + nums[2]
    summ = 12 + (-5)
    summ = 7
 
    j = 3, range = (i + k) => 1 + 4 -> 5 (until 4th index)

    summ = summ + nums[j] -> summ + nums[3]
    summ = 7 + (-6)
    summ = 1

    j = 4, range = (i + k) => 1 + 4 -> 5 (last iteration)

    summ = summ + nums[j] -> summ + nums[4]
    summ = 1 + 50
    summ = 51

    average = summ / k
    -> 51 / 4
    average = 12.75

    max_average = max(max_average, average)
    max_average = max(0.5, 12.75)
    max_average = 12.75

    --------------------------

    i = 2
    summ = 0
    j = 2, range = (i + k) => 2 + 4 -> 6 (so until 5th index)

    summ = summ + nums[j] -> summ + nums[2]
    summ = 0 + (-5)
    summ = -5

    j = 3, range = (i + k) => 2 + 4 -> 6 ( until 5th index)

    summ = summ + nums[j] -> summ + nums[3]
    summ = -5 + (-6)
    summ = -13
 
    j = 4, range = (i + k) => 2 + 4 -> 6 (until 5th index)

    summ = summ + nums[j] -> summ + nums[4]
    summ = -13 + 50
    summ = 37

    j = 5, range = (i + k) => 2 + 4 -> 6 (last iteration)

    summ = summ + nums[j] -> summ + nums[5]
    summ = 37 + 3
    summ = 40

    average = summ / k
    -> 40 / 4
    average = 10

    max_average = max(max_average, average)
    max_average = max(12.75, 10)
    max_average = 12.75

    OUTPUT = max_average = 12.75

'''

# Solution 2 -> Silding Window:

def findMaxAverage2(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum + nums[i] - nums[i - k]
        max_sum = max(window_sum, max_sum)

    return max_sum / float(k)

result2 = findMaxAverage2(nums, k)
print(result2)

'''
TRACING :

nums = [1, 12, -5, -6, 50, 3]
k = 4

window_sum = sum(nums[:k])
window_sum = sum of all elements until k(not included)
           = sum of ele until 4 -> 1 + 12 + (-5) + (-6)
window_sum = 2
max_sum = window_sum = 2

for i in range(k, len(nums)):
    range is from 4 to 6:
    i = 4
        window_sum = window_sum + nums[i] - nums[i - k]
                   = 2 + nums[4] - nums[4 - 4]
                   = 2 + 50 - nums[0]
                   = 52 - (1)
                   = 51
        
        max_sum = max(max_sum, window_sum)
                = max(2, 51)
        max_sum = 51

    i = 5
        window_sum = window_sum + nums[i] - nums[i - k]
                   = 51 + nums[5] - nums[1]
                   = 51 + 3 - 12
                   = 42
        
        max_sum = max(max_sum, window_sum)
                = max(51, 42)
                = 51

        
    max_sum / k => 51 / 4
                = 12.75





'''
