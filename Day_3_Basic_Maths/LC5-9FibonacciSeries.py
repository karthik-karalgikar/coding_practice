def fibRecursion(n):
    if n <= 1:
        return n
    else:
        return fibRecursion(n - 1) + fibRecursion(n - 2)

print(fibRecursion(n=5))

'''
TRACING:

n = 5

n <= 1 -> false
else:
    fibRecursion(4) + fibRecursion(3)

    fibRecursion(4) = fibRecursion(3) + fibRecursion(2) | fibRecursion(3) = fibRecursion(2) + fibRecursion(1)

    fibRecursion(3) = fibRecursion(2) + fibRecursion(1) | fibRecursion(2) = fibRecursion(1) + fibRecursion(0)
    fibRecursion(2) = fibRecursion(1) + fibRecursion(0) | fibRecursion(1) = 1

    fibRecursion(2) = fibRecursion(1) + fibRecursion(0) | fibRecursion(2) = 1 + 0
    fibRecursion(2) = 1 + 0                             | fibRecursion(1) = 1

    fibRecursion(2) = 1 + 0                             | fibRecursion(2) = 1
    fibRecursion(2) = 1                                 | fibRecursion(1) = 1

    Backtracking:
    0 + 1 + 1 + 2 + 3 = 
    
'''
        
