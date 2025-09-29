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

'''
TRACING - 

keyboards = [3, 1]
drives = [5, 2, 8]
b = 10

sum = 0
result = []

for i in range(len(keyboards)):
    -> i = 0
    for j in range(len(drives)):
        -> j = 0
        sum = keyboards[i] + drives[j]
        sum = keyboards[0] + drives[0] -> 3 + 5
        sum = 8

        if sum <= b:
        8 <= 10 -> true
            result.append(sum) 
            result = [8]
            sum = 0

        -> j = 1
        sum = keyboards[i] + drives[j]
        sum = keyboards[0] + drives[1] -> 3 + 2
        sum = 5

        if sum <= b:
        5 <= 10 -> true
            result.append(sum)
            result = [8, 5]
            sum = 0

        -> j = 2
        sum = keyboards[i] + drives[j]
        sum = keyboards[0] + drives[2] -> 3 + 8
        sum = 11

        if sum <= b:
        11 <= 10 -> false

        else:
            continue
            
    -> i = 1
    for j in range(len(drives)):
        -> j = 0
        sum = keyboards[i] + drives[j]
        sum = keyboards[1] + drives[0] -> 1 + 5 
        sum = 6

        if sum <= b:
        6 <= 10 -> true
            result.append(sum)
            result = [8, 5, 6]
            sum = 0

        -> j = 1
        sum = keyboards[i] + drives[j]
        sum = keyboards[1] + drives[1] -> 1 + 2
        sum = 3

        if sum <= b:
        3 <= 10 -> true
            result.append(sum)
            result = [8, 5, 6, 3]
            sum = 0

        -> j = 2
        sum = keyboards[i] + drives[j]
        sum = keyboards[1] + drives[2] -> 1 + 8
        sum = 9

        if sum <= b:
        9 <= 10 -> true
            result.append(sum)
            result = [8, 5, 6, 3, 9]
            sum = 0
        
if len(result) == 0:
len(result) = 5 -> false

else:
    return max(result)

Output = 9

'''