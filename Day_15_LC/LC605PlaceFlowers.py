def canPlaceFlowers(flowerbed, n):
    count = 0

    if n == 0:
        return True
    
    for i in range(len(flowerbed)):
        if i == 0:
            left = 0
        else:
            left = flowerbed[i - 1]

        if i == len(flowerbed) - 1:
            right = 0
        else:
            right = flowerbed[i + 1]

        if left == 0 and right == 0 and flowerbed[i] == 0:
            flowerbed[i] = 1
            count = count + 1
            if count == n:
                return True
            
    if count == n:
        return True
    else:
        return False
    
flowerbed = [1,0,0,0,1]
n = 2
result = canPlaceFlowers(flowerbed, n)
print(result)


'''
TRACING:

flowerbed = [1,0,0,0,1]
n = 2

count = 0

if n == 0 -> false, does not go into the if statement

for i in len(flowerbed):
    i = 0, len(flowerbed) = 5

    if i == 0: -> true
        left = 0

    if i == len(flowerbed) - 1 -> i == 4 -> false
    else:
        right = flowerbed[i + 1] -> flowerbed[0 + 1] -> flowerbed[1]
        right = flowerbed[1] => 0
        right = 0

    if left == 0 and right == 0 and flowerbed[i] == 0:
        left == 0 -> true
        right == 0 -> true
        flowerbed[0] == 0 -> false (flowerbed[0] == 1)

    count = 0 

    -------------------------

    i = 1, len(flowerbed) == 5

    if i == 0 -> false
    else: 
        left = flowerbed[i - 1] -> flowerbed[1 - 1] -> flowerbed[0]
        left = 1

    if i == len(flowerbed) - 1 -> 5 - 1 -> 4 => false
    else:
        right = flowerbed[i + 1] -> flowerbed[1 + 1] -> flowerbed[2]
        right = 0

    if left == 0 and right == 0 and flowerbed[i] == 0:
        left = 1 
        does not go inside if statement

    count = 0

    -------------------------
    
    i = 2, len(flowerbed) = 5

    if i == 0 -> false
    else:
        left = flowerbed[i - 1] -> flowerbed[2 - 1] -> flowerbed[1]
        left = 0

    if i == len(flowerbed) - 1 -> 5 - 1 -> 4 -> false
    else:
        right = flowerbed[i + 1] -> flowerbed[2 + 1] -> flowerbed[3]
        right = 0

    if left == 0 and right == 0 and flowerbed[i] == 0:
        left == 0
        right == 0
        flowerbed[2] == 0

        flowebed[2] = 1
        count = count + 1 -> 0 + 1
        count = 1

        if count == n:
            1 == 2: -> false 
            does not go inside if statement

    count = 1
    flowerbed[2] = 1

    -------------------------

    i = 3, len(flowerbed) = 5

    if i == 0 -> false
    else:
        left = flowerbed[i - 1] -> flowerbed[3 - 1] -> flowerbed[2]
        left = 1

    if i == len(flowerbed) - 1 -> 5 - 1 -> 4 -> false
    else:
        right = flowerbed[i + 1] -> flowerbed[3 + 1] -> flowerbed[4]
        right = 1

    if left == 0 and right == 0 and flowerbed[i] == 0:
        left = 1
        does not go inside if statement

    count = 1

    -------------------------

    i = 4, len(flowerbed) = 5

    if i == 0 -> false
    else:
        left = flowerbed[i - 1] -> flowerbed[4 - 1] -> flowerbed[3]
        left = 0

    if i == len(flowerbed) - 1 -> 4 -> true:
        right = 0

    if left == 0 and right == 0 and flowerbed[i] == 0:
        left == 0
        right == 0
        flowerbed[4] == 1
        does not go inside the if statement

    count = 1

    if count == n:
        1 == 2 -> False

        so False is returned.

    Output - False

'''