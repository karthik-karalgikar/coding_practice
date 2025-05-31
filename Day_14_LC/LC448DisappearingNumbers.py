def findDisappearedNumbers(nums):
    numSet = set(nums)
    temp = []

    for i in range(len(nums) + 1):
        if i not in numSet:
            temp.append(i)
    
    return temp[1:]

nums = [1, 2, 4, 6, 6, 7, 9, 10]
result = findDisappearedNumbers(nums)
print(result)

'''
TRACING 

nums = [1, 2, 4, 6, 6, 7, 9, 10]
numSet = set(nums) => {1,2,4,5,7,9,10}
temp = []

for loop:
len(nums) + 1 => 8 + 1 => 9
i = 0 
    if i not in numSet:
        0 not in {1,2,4,5,7,9,10} -> true
        temp.append(i) -> temp.append(0)
        => temp =[0]

i = 1
    if i not in numSet:
        1 not in {1,2,4,5,7,9,10} -> false

i = 2
    if i not in numSet:
        2 not in {1,2,4,5,7,9,10} -> false

i = 3
    if i not in numSet:
        3 not in {1,2,4,5,7,9,10} -> true
        temp.append(i) -> temp.append(3)
        => temp = [0, 3]

i = 4
    if i not in numSet:
        4 not in {1,2,4,5,7,9,10} -> false

i = 5
    if i not in numSet:
        5 not in {1,2,4,5,7,9,10} -> false

i = 6
    if i not in numSet:
        6 not in {1,2,4,5,7,9,10} -> true
        temp.append(i) -> temp.append(6)
        => temp = [0, 3, 6]

i = 7
    if i not in numSet:
        7 not in {1,2,4,5,7,9,10} -> false
    
i = 8
    if i not in numSet:
        8 not in {1,2,4,5,7,9,10} -> true
        temp.append(i) -> temp.append(8)
        => temp = [0, 3, 6, 8]

loop ends

return temp[1:] -> temp[1:] = [3, 6, 8]

'''