def catAndMouse(x, y, z):
    catA = abs(x - z)
    catB = abs(y - z)
    
    if catA < catB:
        return 'Cat A'
    elif catB < catA:
        return 'Cat B'
    else:
        return 'Mouse C'
    
print(catAndMouse(2, 5, 4))

'''
TRACING -
x = position of cat A
y = position of cat B
z = position of Mouse C

catA = abs(x - z)
catA = abs(2 - 4)
catA = 2

catB = abs(y - z)
catB = abs(5 - 4)
catB = 1

if catA < catB:
2 < 1 -> false

elif catB < catA:
1 < 2 -> true
    return 'Cat B'

Output = Cat B
'''