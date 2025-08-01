def climbStairs(n):
    if n == 0 or n == 1:
        return 1
    n1, n2 = 1, 1
    for i in range(2, n + 1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    
    return n2

print(climbStairs(n = 4))

'''
TRACING : 

same as fibonacci series. 

'''