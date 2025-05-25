#Reverse a number

def reverse(n):
    rev = 0
    while n != 0:
        digit = n % 10 
        rev = rev * 10 + digit
        n = n // 10
    return rev

result = reverse(123)
print(result)

# Output - 321

'''
TRACING: 
n = 123 and rev = 0

Step 1:
digit = 123 % 10 = 3(remainder)
rev = 0 * 10 + 3 => 0 + 3 => 3
rev = 3
n = 123 // 10 => n = 12

Step 2:
digit = 12 % 10 = 2
rev = 3 * 10 + 2 => 30 + 2 => 32
n = 12 // 10 => n = 1

Step 3:
digit = 1 % 10 = 1
rev = 32 * 10 + 1 => rev = 321
n = 1 // 10 = 0

Exit while loop, return rev = 321

'''

# VARIATION: 
# For negative numbers: 

import math 

def reverse(n):
    MAX_INT = 2 ** 31 - 1
    MIN_INT = -2 ** 31
    rev = 0
    while n != 0:
        if rev > MAX_INT / 10 or rev < MIN_INT / 10:
          return 0
        digit = n % 10 if n > 0 else n % -10
        rev = rev * 10 + digit
        n = math.trunc(n / 10)
    return rev

result = reverse(-123)
print(result)

# OUTPUT: -321