def printdivisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end = " ")
    print()

printdivisors(36)

'''
TRACING:
n = 36
for loop starting from 1 and ends at 36
36 % 1 == 0 -> yes, print 1
36 % 2 == 0 -> yes, print 2 
36 % 3 == 0 -> yes, print 3
36 % 4 == 0 -> yes, print 4
36 % 5 == 0 -> no
36 % 6 == 0 -> yes, print 6
36 % 7 == 0 -> no
36 % 8 == 0 -> no
36 % 9 == 0 -> yes, print 9
36 % 10 == 0 -> no
.
.
26 % 10 == 0 -> yes, print 36

'''

# Solution 2

def printdivisors(n):
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            print(i, end = " ")
            if i != n / i:
                print(int(n/i), end=" ")
    print()

printdivisors(36)

'''
TRACING 
n = 36
for loop starts from 1 and ends at root(36)
36 % 1 == 0 -> yes, print 1
1 != 36/1 -> yes, print 36
36 % 2 == 0 -> yes, print 2
2 != 36/2, i.e., 2 != 18 -> yes, print 18
36 % 3 == 0 -> yes, print 3
3 != 36/3, i.e., 3 != 12 -> yes, print 12
36 % 4 == 0 -> yes, print 4
4 != 36/4, i.e., 4 != 9 -> yes, print 9
36 % 5 == 0, no
36 % 6 == 0 -> yes, print 6
6 != 36/6 -> no
'''