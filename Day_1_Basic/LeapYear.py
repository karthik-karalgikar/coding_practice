'''
Write a program that works out whether if a given year is a leap year.
Knowledge required before coding: 
1) on every year that is evenly divisible by 4 
2) **except** every year that is evenly divisible by 100 
3) **unless** the year is also evenly divisible by 400
'''

# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.


year = int(input("Which year do you want to check? "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")   


# Variation: 
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            # the "else:" clause isn't really needed for these
            return False
        return True
    return False

year = int(input("Check year"))
print(is_leap(year))