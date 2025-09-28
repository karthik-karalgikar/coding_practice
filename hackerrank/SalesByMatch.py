def sockMerchant(ar):
    # Write your code here
    frequency = {}
    count = 0
    
    for i in ar:
        if i in frequency:
            frequency[i] = frequency[i] + 1
        else:
            frequency[i] = 1
            
    for i in frequency:
        if frequency[i] == 1:
            continue
        else:
            count = count + (frequency[i] // 2)
            
    return count

print(sockMerchant([1,2,1,2,1,3,2]))
'''
TRACING - 

freq = {}

for i in ar:
    -> i = 1
    if i in freq:
    1 in freq -> false

    else:
        freq[i] = 1

    freq = {1 : 1}

    -> i = 2
    if i in freq:
    2 in freq -> false

    else:
        freq[i] = 1

    freq = {1 : 1, 2 : 1}

    -> i = 1
    if i in freq:
        freq[i] = freq[i] + 1
        freq[1] = 1 + 1

    freq = {1 : 2, 2 : 1}

    -> i = 2
    if i in freq:
        freq[i] = freq[i] + 1
        freq[i] = 1 + 1

    freq = {1 : 2, 2 : 2}

    -> i = 1
    if i in freq:
        freq[i] = freq[i] + 1
        freq[i] = 2 + 1

    freq = {1 : 3, 2 : 2}
    
    -> i = 3
    if i in freq:
    3 in freq -> false

    else:
        freq[3] = 1

    freq = {1 : 3, 2 : 2, 3 : 1}

    -> i = 2
    if i in freq:
        freq[i] = freq[i] + 1
        freq[i] = 2 + 1

    freq = {
            1 : 3, 
            2 : 3, 
            3 : 1
        }
    
for i in freq:
    -> i = 1
    if freq[i] == 1 -> false

    else:
        count = count + (freq[i] // 2)
        count = 0 + (3 // 2)
        count = 0 + 1
        count = 1

    -> i = 2
    if freq[i] == 1 -> false

    else:
        count = count + (freq[i] // 2)
        count = 1 + (3 // 2)
        count = 1 + 1
        count = 2

    -> i = 3
    if freq[i] == 1 -> true
        continue

return count 

Output = 2

'''
