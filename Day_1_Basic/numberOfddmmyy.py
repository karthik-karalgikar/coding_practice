'''
Create a program using maths and f-Strings that tells us how many days, 
weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with 
our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.
'''


years = input("What is your current age?")
age = int(years)
b = 90 - age
weeks = b*52
days = b*365
months = b*12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")


# TRACING : 
# age = 56
# b = 90 - 56, i.e., 34
# weeks = 34*52 = 1768
# days = 34*365 = 12410
# months = 34*12 = 408

# OUTPUT - You have 12410 days, 1768 weeks, and 408 months left.