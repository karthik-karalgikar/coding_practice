'''
Write a function that capitalizes the 1st and 4th letters of a name
'''

def cap(name):
    first_letter = name[0]
    in_between = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper() + in_between + fourth_letter.upper() + rest

def cap1(name):
    first_half = name[:3]
    second_half = name[3:]
    
    return first_half.capitalize() + second_half.capitalize()

name = "karthik"
res = cap(name)
res1 = cap1(name)
print(res)
print(res1)