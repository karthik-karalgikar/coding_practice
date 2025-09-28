def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    result = []
    sum = 0
    
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            sum = keyboards[i] + drives[j]
            if sum <= b:
                result.append(sum)
                sum = 0
            else:
                continue
                
    if len(result) == 0:
        return -1
    else:
        return max(result)
    
print(getMoneySpent([3, 1], [5, 2, 8], 10))