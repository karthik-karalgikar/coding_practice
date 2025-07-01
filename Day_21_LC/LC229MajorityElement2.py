def MissingNumber2(nums):
    frequency = {}
    result = []
    n = len(nums)

    for i in nums:
        if i in frequency:
            frequency[i] = frequency[i] + 1
        else:
            frequency[i] = 1

    for i in frequency:
        if frequency[i] > n / 3:
            result.append(i)

    return result

print(MissingNumber2(nums=[3, 2, 3]))

'''
TRACING :

nums = [3,2,3]

frequency = {}
result = []
n = len(nums) -> 3

n / 3 -> 3/3 -> 1

for i in nums:
    -> i = 3
    if i in frequency -> False
    else:
        frequency[i] = 1
        frequency[3] = 1
        frequency = {3 : 1}

    -> i = 2
    for i in frequency -> False
    else:
    frequency[i] = 1
    frequency[2] = 1
    frequency = {3 : 1, 2 : 1}

    -> i = 3
    if i in frequency -> True
        frequency[i] = frequency[i] + 1
        frequency = {3 : 2, 2 : 1}

for i in frequency:
    -> i = 3
    if frequency[i] > n / 3:
    frequency[3] = 2
    n / 3 = 1

    True

    result.append(i)
    result.append(3)

    result = [3]

    -> i = 2
    if frequency[i] > n / 3:
    frequency[2] = 1
    False

return result 

Output = [3]

'''