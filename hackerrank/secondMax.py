# n = int(input())
# arr = map(int, input().split())

def secondMax(arr):   
    maxx = -101
    secondMax = -101
        
    for i in arr:
        if i > maxx:
            secondMax = maxx 
            maxx = i
        elif i > secondMax and i < maxx:
            secondMax = i
                
    return secondMax

arr = [2, 3, 6, 6, 5]
print(secondMax(arr))

'''
TRACING :

arr = [2, 3, 6, 6, 5]

max = -101
secondMax = -101

for i in arr:
    -> i = 2
    if i > max:
    2 > -101 -> true
        secondMax = max
        secondMax = -101
        max = i 
        max = 2

    -> i = 3
    if i > max:
    3 > 2 -> true
        secondMax = max
        secondMax = 2
        max = i
        max = 3

    -> i = 6
    if i > max:
    6 > 3 -> true
        secondMax = max
        secondMax = 3
        max = i
        max = 6

    -> i = 6
    if i > max:
    6 > 6 -> false

    elif i > secondMax and i < max:
    6 > 3 -> true and 6 < 6 -> false
    does not go inside elif statement

    -> i = 5
    if i > max: 
    5 > 6 -> false

    elif i > secondMax and i < max:
    5 > 3 -> true and 5 < 6 -> true
        secondMax = i
        secondMax = 5

    retun secondMax 

    Output = 5

'''