def ThirdLargest(nums):
    numSet = set(nums)

    if len(numSet) == 0 or len(numSet) == 1 or len(numSet) == 2:
        return max(numSet)

    numSetsort = sorted(numSet)
    thirdLarge = numSetsort[len(numSet) - 3]

    return thirdLarge

nums = [1,1]
res = ThirdLargest(nums)
print(res)


'''
TRACING :
nums = [3,2,1]
numSet = set(nums) => {3,2,1}

len(numSet) == 3, so it does not go inside if statement

numSetsort = sorted(numSet) => {1,2,3}
thirdLarge = numSetsort[len(numSet) - 3] => numSetsort[3 - 3]
=> numSetsort[0] -> 1

output = Third largest number = 1

nums = [1,1]
numSet = set(nums) => {1}

len(numSet) == 1, so it goes inside if statement:
return max(numSet) => max({1}) => 1


'''