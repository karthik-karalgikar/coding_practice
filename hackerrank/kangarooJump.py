#Solution 1 works, but gets TLE for some

def kangaroo(x1, v1, x2, v2):
    if v1 <= v2 and x1 < x2:
        return "NO"
    if v2 <= v1 and x2 <= x1:
        return "NO"
    
    while x1 <=10000 and x2 <= 10000:
        if x1 == x2:
            return "YES"
        x1 = x1 + v1
        x2 = x2 + v2
        
    return "NO"

print(kangaroo(0, 2, 5, 3))


#Solution 2 -

def kangaroo2(x1, v1, x2, v2):
    if x1 > x2 and v1 > v2:
        return "NO"
    if x2 > x1 and v2 > v1:
        return "NO"
    if v1 == v2:
        return "NO"
    
    return "YES" if (x2 - x1) % (v1 - v2) == 0 else "NO"

print(kangaroo2(0, 2, 5, 3))

'''
TRACING - 

Example 1:

x1 = 0, v1 = 2
x2 = 5, v2 = 3

if x1 > x2 and v1 > v2:
-> 0 > 5 and 2 > 3 -> 0 and 0 -> false

if x2 > x1 and v2 > v1:
-> 5 > 0 and 3 > 2 -> 1 and 1 -> True
    return "NO"

Example 2:

x1 = 0, v1 = 3
x2 = 4, v2 = 2

if x1 > x2 and v1 > v2:
-> 0 > 4 and 3 > 2 -> 0 and 1 -> false

if x2 > x1 and v2 > v1:
-> 4 > 0 and 2 > 3 -> 1 and 0 -> false

if v1 == v2: 
-> 3 == 2 -> false

(x2 - x1) % (v1 - v2) == 0
(4 - 0) % (3 - 2) == 0
4 % 1 == 0
0 == 0 -> true

"YES"
'''