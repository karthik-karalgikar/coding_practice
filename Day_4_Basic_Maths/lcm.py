def lcm(a, b):
    g = gcd(a, b)
    lcm = (a * b) // g
    return lcm

def gcd(a, b):
    if b == 0:
        return a
    return gcd(a, a % b)

print(lcm(2, 4))

'''
TRACING - 

a = 2, b = 4

g = gcd(a, b) -> gcd(2, 4)

if b == 0 -> false

return gcd(a, a % b) -> gcd(2, 2 % 4)
return gcd(2, 2)

if b == 0 -> false

return gcd(a, a % b) -> gcd(2, 2 % 2)
return gcd(2, 0)

if b == 0 -> true
    return a 
    => return 2

g = 2
lcm = (a * b) // g
lcm = (2 * 4) // 2
lcm = 8 // 2
lcm = 4

'''
