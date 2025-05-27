'''
Given two integers, return true if the sum of integers is 20 or if one of the integers
is 20. If not, return false
'''

def twenty(a,b):
    if a + b == 20 or a == 20 or b == 20:
        result = True
    else:
        result = False

    return result

a = 200
b = 40 
result = twenty(a, b)
print(result)