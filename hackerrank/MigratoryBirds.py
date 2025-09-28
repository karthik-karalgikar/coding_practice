def migratoryBirds(arr):
    frequency = {}

    for i in arr:
        if i in frequency:
            frequency[i] = frequency[i] + 1
        else:
            frequency[i] = 1

    max_freq = 0
    bird_id = None
    for i, j in frequency.items():
        if j > max_freq or (j == max_freq and i < bird_id):
            max_freq = j
            bird_id = i

    return bird_id

print(migratoryBirds(arr=[1,1,2,2,3]))
'''
TRACING - 
arr = [1, 1, 2, 2, 3]

frequency = {}

for i in arr:
-> i = 1
    if i in frequency:
    1 in frequency -> false
    
    else:
        frequency[i] = 1
        frequency[1] = 1

frequency = {1 : 1}

-> i = 1
    if i in frequency: 
    i in frequency -> True
        frequency[i] = frequency[i] + 1
        frequency[1] = 1 + 1
        frequency[1] = 2

frequency = {1 : 2}

-> i = 2
    if i in frequency:
    2 in frequency -> false
    
    else:
        frequency[2] = 1
        frequency[2] = 1

frequency = {1 : 2, 2 : 1}

-> i = 2
    if i in frequency: 
    i in frequency -> True
        frequency[i] = frequency[i] + 1
        frequency[2] = 1 + 1
        frequency[2] = 2

frequency = {1 : 2, 2 : 2}

-> i = 3
    if i in frequency:
    3 in frequency -> false
    
    else:
        frequency[i] = 1
        frequency[3] = 1

frequency = {
            1 : 2, 
            2 : 2, 
            3 : 1
        }


max_freq = 0
bird_id = None

for i, j in frequency.items():
    
    -> i = 1, j = 2
    if j > max_freq or (j == max_freq and i < bird_id):
    2 > 0 -> true
        max_freq = j
        max_freq = 2

        bird_id = i
        bird_id = 1

    -> i = 2, j = 2
    if j > max_freq or (j == max_freq and i < bird_id):
    2 > 2 -> false
    j == max_freq and i < bird_id -> j == 2(true) and 2 < 1(false) -> false

    -> i = 3, j = 1
    if j > max_freq or (j == max_freq and i < bird_id):
    3 > 2 -> false
    j == max_freq -> 1 == 2 -> false

return bird_id
return 1

Output = 1

    
'''