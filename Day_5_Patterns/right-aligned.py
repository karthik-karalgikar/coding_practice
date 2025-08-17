def staircase(n):
    # Write your code here
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)

staircase(4)


'''
TRACING :

n = 4

for i in range(1, n + 1):
    -> i = 1
    print(" " * (n - i) + "#" * i)
    print(" " * (4 - 1) + "#" * 1)
    print(" " * 3 + "#" * 1)
    o/p =    # (3 whitespace)

    -> i = 2
    print(" " * (n - i) + "#" * i)
    print(" " * (4 - 2) + "#" * 2)
    print(" " * 2 + "#" * 2)
    o/p =   ## (2 whitespace)

    -> i = 3
    print(" " * (n - i) + "#" * i)
    print(" " * (4 - 3) + "#" * 3)
    print(" " * 1 + "#" * 3)
    o/p =  ### (1 whitespace)

    -> i = 4
    print(" " * (n - i) + "#" * i)
    print(" " * (4 - 4) + "#" * 4)
    print(" " * 0 + "#" * 4)
    o/p = #### (o whitespace)

calling the function ->
   #
  ##
 ###
####

'''