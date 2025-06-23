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
    fibRecursion(3) = fibRecursion(2) + fibRecursion(1)
    fibRecursion(3) = fibRecursion(1) + fibRecursion(0) + 1
    fibRecursion(3) = 1 + 0 + 1
    fibRecursion(3) = 2

    fibRecursion(4) = fibRecursion(3) + fibRecursion(2)
    fibRecursion(4) = fibRecursion(2) + fibRecursion(1) + fibRecursion(1) + fibRecursion(0)
    fibRecursion(4) = fibRecursion(1) + fibRecursion(0) + 1 + 1 + 0
    fibRecursion(4) = 1 + 0 + 1 + 1 + 0
    fibRecursion(4) = 3

    fibRecursion(5) = fibRecursion(4) + fibRecursion(3)
    fibRecursion(5) = 3 + 2
    fibRecursion(5) = 5
    
'''

def fibIteration(n):
    n1 = 0
    n2 = 1

    for i in range(2, n + 1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        # i = i + 1

    return n3

print(fibIteration(n=5))     
