def countingValleys(path):
    # Write your code here
    pathList = list(path)
    sum = 0
    count = 0
    
    for i in pathList:
        if i == 'U':
            sum = sum + 1
        elif i == "D":
            sum = sum - 1
            
        if sum == 0 and i == 'U':
            count = count + 1
        
    return count - 1
    
print(countingValleys("UDDDUDUU"))

'''
TRACING - 
path = UDDDUDUU

pathList = ["U", "D", "D", "D", "U", "D", "U", "U"]
sum = 0
count = 0

for i in pathList:
    -> i = 'U'
    if i == 'U':
        sum = sum + 1
        sum = 1

    <not checking the if sum == 0 if statement, because......too much work>

    -> i = 'D'
    elif i == 'D':
        sum = sum - 1
        sum = 0

    will not go into if statement because i is D

    -> i = 'D'
    elif i == 'D':
        sum = sum - 1
        sum = -1

    -> i = 'D'
    elif i == 'D':
        sum = sum - 1
        sum = -2

    -> i = 'U'
    if i == 'U':
        sum = sum + 1
        sum = -1

    -> i = 'D'
    elif i == 'D':
        sum = sum - 1
        sum = -2

    -> i = 'U'
    if i == 'U'
        sum = sum + 1
        sum = -1

    -> i = 'U'
    if i == 'U'
        sum = sum + 1
        sum = 0

    if sum == 0 and i == 'U': -> true
        count = count + 1
        count = 1

return count 

output = 1
'''