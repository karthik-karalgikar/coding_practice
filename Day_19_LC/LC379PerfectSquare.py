#note - do not use sqrt

def isPerfectSquare(num):
    if num < 2:
        return True

    left = 2
    right = num // 2
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1

    return False

print(isPerfectSquare(num=16))


'''
TRACING: 

num = 16

if num < 2: -> False

left = 2
right = num // 2 -> 16 // 2
right = 8

while left <= right:
    -> 2 < 8 -> true
    
    mid = (left + right) // 2
    mid = (2 + 8) // 2 -> 10 // 2
    mid = 5

    square = mid * mid -> 5 * 5
    square = 25

    if square == num: -> 16 == 25 -> False

    elif sqaure < num: -> 25 < 16 -> False

    else:
        right = mid - 1
        right = 5 - 1 
        right = 4

    -> 2 <= 4 -> True

    mid = (left + right) // 2
    mid = (2 + 4) // 2 -> 6 // 2
    mid = 3

    square = mid * mid  -> 3 * 3
    square = 9

    if square == num: -> 16 == 9 -> False

    elif square < num: 
        9 < 16 -> True
        left = mid + 1
        left = 3 + 1
        left = 4

    -> 4 <= 4 -> True

    mid = (left + right) // 2
    mid = (4 + 4) // 2
    mid = 4

    square = mid * mid
    square = 16

    if square = mid * mid -> 4 * 4:
        square = 16
        return True

        



'''