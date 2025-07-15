def removeElement(nums, val):
    count = 0
    for i in nums:
        if i == val:
            count = count + 1

    return count

print(removeElement(nums=[3, 2, 2, 3], val=3))