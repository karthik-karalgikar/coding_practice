# Write a function that checks whether the number passed into
# it is a prime number or not.

def prime_checker(n):
    for i in range(2,n):
       if n % i == 0:
           print("It's not a prime number.")
           break
    else:
        print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(n)


# Output: 
# 73 
# It's a prime number.
# 24
# It's not a prime number.

# TRACING : 
# n = 13
# for loop,
# i = 2
# 13 % 2 == 1
# 13 % 3 == 1
# 13 % 4 == 1
# 13 % 5 == 3
# 13 % 6 == 1
# 13 % 7 == 6
# 13 % 8 == 5
# 13 % 9 == 4
# 13 % 10 == 3
# 13 % 11 == 2
# 13 % 12 == 1
# End for loop, print "It's a prime number"

# n = 9
# for loop, 
# i = 2
# 9 % 2 == 1
# 9 % 3 == 0
# If condition satisfied, print "It's not a prime number"