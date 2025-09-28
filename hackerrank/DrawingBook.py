def pageCount(n, p):
    low = p // 2
    if n % 2 == 1:
        high = (n - p) // 2
    else:
        high = (n - p + 1) // 2

    return min(low, high)

print(pageCount(6, 3))

'''
TRACING - 

n = 6 (total number of pages)
p = 3 (the page we have to turn to)

low = p // 2 -> 3 // 2 
low = 1

if n % 2 == 1:
6 % 2 == 0 -> false

else:
    high = (n - p + 1) // 2
    high = (6 - 3 + 1) // 2
    high = 4 // 2
    high = 2

return min(low, high)

min(1, 2)

output = 1
'''