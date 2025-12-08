'''
Write a program that adds the digits in a 2 digit number.
e.g. if the input was 35, then the output should be 3 + 5 = 8

Example Input
39
Example Output
3 + 9 = 12
12
'''

def twoDigitSum(two_digit_number):
    sum = 0
    if len(str(two_digit_number)) == 2:
        while(two_digit_number != 0):
            sum = sum + (two_digit_number % 10)       
            two_digit_number = two_digit_number//10 
    else: 
        print("Please enter 2 digit")  
                                            
    return sum

# two_digit_number = int(input("Type a two digit number: "))
two_digit_number = 34
print(twoDigitSum(two_digit_number))


# TRACING : 
 # sum = 0 + (39 % 10) i.e., 0 + (9) = 9. Therefore, sum = 9
 # two_digit_number = 39//10 = 3
 # sum = 9 + (3 % 10) i.e,. 9 + (3) = 12. Therefore, sum = 12
 # two_digit_number = 3//10 = 0. 
 # While loop condition true. 
 # print sum. 

def numberSum(number):
   sum = 0
   while number != 0:
      sum = sum + (number % 10)
      number = number // 10

   return sum

number = 339
print(numberSum(number))
