def divisibleSumPairs(k, ar):
    # Write your code here
    count = 0
    
    for i in range(len(ar)):
        for j in range(1, len(ar)):
            if i < j and (ar[i] + ar[j]) % k == 0:
                count = count + 1
                
    return count

print(divisibleSumPairs(ar=[1, 2, 3, 4, 5, 6], k = 5))

'''
TRACING -
 
ar = [1, 2, 3, 4, 5, 6]
k = 5
len(ar) = 6

count = 0

for i in range(len(ar)):
    -> i = 0
    for j in range(1, len(ar)):
        -> j = 1
        if i < j and (ar[i] + ar[j]) % k == 0:
        0 < 1 -> true
        (ar[0] + ar[1]) % k == 0 -> (1 + 2) % 5 -> 
        3 % 4 == 0 -> false

        -> j = 2
        if i < j and (ar[i] + ar[j]) % k == 0:
        0 < 2 -> true
        (ar[0] + ar[1]) % k == 0 -> (1 + 3) % 5 -> 
        4 % 5 == 0 -> false

        -> j = 3
        if i < j and (ar[i] + ar[j]) % k == 0:
        0 < 3 -> true
        (ar[0] + ar[3]) % k == 0 -> (1 + 4) % 5 -> 
        5 % 5 == 0 -> true
            count = count + 1
            count = 1

        -> j = 4
        if i < j and (ar[i] + ar[j]) % k == 0:
        0 < 4 -> true
        (ar[0] + ar[4]) % k == 0 -> (1 + 5) % 5 -> 
        6 % 5 == 0 -> false

        -> j = 5
        if i < j and (ar[i] + ar[j]) % k == 0:
        0 < 5 -> true
        (ar[0] + ar[5]) % k == 0 -> (1 + 6) % 5 -> 
        7 % 5 == 0 -> false

    -> i = 1
    for j in range(1, len(ar)):
        -> j = 1
        if i < j and (ar[i] + ar[j]) % k == 0:
        1 < 1 -> false

        -> j = 2
        if i < j and (ar[i] + ar[j]) % k == 0:
        1 < 2 -> true
        (ar[1] + ar[2]) % k == 0 -> (2 + 3) % 5 ->
        5 % 5 == 0 -> true
            count = count + 1
            count = 2

        -> j = 3
        if i < j and (ar[i] + ar[j]) % k == 0:
        1 < 3 -> true
        (ar[1] + ar[3]) % k == 0 -> (2 + 4) % 5 -> 
        6 % 5 == 0 -> false

        -> j = 4
        if i < j and (ar[i] + ar[j]) % k == 0:
        1 < 4 -> true
        (ar[1] + ar[4]) % k == 0 -> (2 + 5) % 5 ->
        7 % 5 == 0 -> false

        .
        .
        .
        .
        .
        .
        .
        .
        .

output = 3
'''
