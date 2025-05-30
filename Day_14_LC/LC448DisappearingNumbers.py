def findDisappearedNumbers(nums):
    numSet = set(nums)
    temp = []

    for i in range(len(nums) ):
        if i not in numSet:
            temp.append(i)
    
    return temp[1:]

nums = [1, 2, 4, 6, 6, 7, 9, 10]
result = findDisappearedNumbers(nums)
print(result)