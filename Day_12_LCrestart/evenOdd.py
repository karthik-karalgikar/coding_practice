'''
write a program that returns lesser of two given number if both are even, but 
returns greater if one or both numbers are odd
'''

def oddEven(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            result = a
        else:
            result = b

    elif a > b:
        result = a
    else:
        result = b

    return result

def oddEven2(a, b):
    if a % 2 == 0 and b % 2 == 0:
        result = min(a,b)
    else:
        result = max(a,b)
    
    return result

a = 7
b = 3
res = oddEven(a, b)
res2 = oddEven2(a,b)
print(res)
print(res2)
