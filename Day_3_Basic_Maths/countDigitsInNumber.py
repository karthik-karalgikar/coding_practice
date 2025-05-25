'''
// Count digits in a number
// Problem Statement: Given an integer N, 
   write a program to count the number of digits in N.
'''
#Solution 1

def count_digits(n):
       count=0
       x=n
       while( x != 0 ):
               x//=10
               count+=1
       return count

n = 12345
print("Number of digits in ",n," is ",count_digits(n)) 


# TRACING : 
# n = 12345
# Step 1: 12345//10 = 1234 -> count = 1
# Step 2: 1234//10 = 123   -> count = 2
# Step 3: 123//10 = 12     -> count = 3
# Step 4: 12//10 = 1       -> count = 4
# Step 5: 1//10 = 0        -> count = 5
# Step 6: Exit loop, return count


#Solution 2

def count_digits(n):
  x = str(n)
  return len(x)

n = 12345
print("Number of digits in ", n, " is ", count_digits(n))

# TRACING:
# n = 12345
# x = '12345'
# len(x) = 5, return 5