def mySqrt(x):
    if x < 0:
        return False

    if x == 1:
        return 1
        
    low = 1
    high = x

    while low <= high:
        mid = (high + low) // 2
        if mid * mid == int(x):
            return int(round(mid))

        elif (mid * mid < int(x)):
            low = mid + 1
        else:
            high = mid - 1

    return int(round(high))

print(mySqrt(3))

'''
TRACING : 

x = 3

low = 1
high = 3

while low <= high:
    1 <= 3 -> true
    mid = (low + high) // 2
    mid = (1 + 3) // 2 -> 4 // 2
    mid = 2

    if mid * mid == int(x):
        2 * 2 = 4 == 3 -> false

    elif mid * mid < int(x):
        4 < 3 -> false

    else:
        high = mid - 1 -> 2 - 1
        high = 1

    low = 1
    high = 1

    1 <= 1 -> true
    mid = (low + high) // 2
    mid = (1 + 1) // 2
    mid = 1

    if mid * mid == int(x):
        1 * 1 = 1 == 3 -> false

    elif mid * mid < int(x):
        1 < 3 -> true
        low = mid + 1 -> 1 + 1
        low = 2

    low = 2
    high = 1

    2 <= 1 -> false

return round(int(high))

Output = 1
    
'''