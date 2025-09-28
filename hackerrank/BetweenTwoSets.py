import math

def getTotalX(A, B):
    def lcm(a, b):
        return a * b // math.gcd(a, b)
    
    lcmA = A[0]
    for i in range(1, len(A)):
        lcmA = lcm(lcmA, A[i])
    
    gcdB = B[0]
    for i in range(1, len(B)):
        gcdB = math.gcd(gcdB, B[i])
    
    count = 0
    x = lcmA
    while x <= gcdB:
        if gcdB % x == 0:
            count += 1
        x += lcmA
    
    return count

'''
TRACING - 

a = [3, 4]
b = [24, 48]

lcmA = a[0]
lcmA = 3
for i in range(1, len(a))
    
    -> i = 1, until 2
    lcmA = lcm(lcmA, a[i])
    lcmA = lcm(3, 4)

    lcm(3, 4)
        return a * b // math.gcd(a, a % b)
        return 3 * 4 // math.gcd(3, 3 % 4)
        return 12 // math.gcd(3, 3)
        return 12 // math.gcd(3, 3 % 3)
        return 12 // math.gcd(3, 0)
        return 12 // 3
        return 4

    lcmA = 4

gcdB = b[0]
gcdB = 24
for i in range(1, len(b))

    -> i = 1, until 2

    gcdB = math.gcd(gcdB, b[i])
    gcdB = math.gcd(24, b[1])
    gcdB = math.gcd(24, 48)
    gcdB = math.gcd(24, 24 % 48)
    gcdB = math.gcd(24, 24)
    gcdB = math.gcd(24, 24 % 24)
    gcdB = math.gcd(24, 0)
    gcdB = 24

    gcdB = 24

count = 0
x = lcmA
x = 4

while x <= gcdB:
    4 <= 24 -> true
        if gcdB % x == 0 -> 24 % 4 == 0 -> true
            count = count + 1
            count = 1

        x = x + lcmA
        x = 4 + 4
        x = 8
    
    8 <= 24 -> true
        if gcdB % x -> 24 % 8 == 0 -> true
            count = count + 1
            count = 2

        x = x + lcmA
        x = 8 + 8
        x = 16

    16 <= 24 -> true
        if gcdB % x -> 24 % 16 == 0 -> false

        x = x + lcmA
        x = 16 + 16
        x = 32

    32 <= 24 -> false

    return count 

    output = 2
'''