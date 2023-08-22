'''
Write a program that adds the digits in a 2 digit number.
e.g. if the input was 35, then the output should be 3 + 5 = 8

Example Input
39
Example Output
3 + 9 = 12
12
'''

two_digit_number = int(input("Type a two digit number: "))

sum = 0
while(two_digit_number != 0):
    sum = sum + (two_digit_number % 10)       
    two_digit_number = two_digit_number//10    
                                          
print(sum)


# TRACING : 
 # sum = 0 + (39 % 10) i.e., 0 + (9) = 9. Therefore, sum = 9
 # two_digit_number = 39//10 = 3
 # sum = 9 + (3 % 10) i.e,. 9 + (3) = 12. Therefore, sum = 12
 # two_digit_number = 3//10 = 0. 
 # While loop condition true. 
 # print sum. 