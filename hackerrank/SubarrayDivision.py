def birthday(s, d, m):
    i = 0
    j = m
    count = 0

    while j <= len(s):
        if sum(s[i : j]) == d:
            count = count + 1

        i = i + 1
        j = j + 1

    return count 

print(birthday(s=[2, 2, 1, 3, 2], d = 4, m = 2))

'''
TRACING -

s = [2, 2, 1, 3, 2]
d = 4
m = 2

i = 0
j = m
count = 0

while j <= len(s): 
    -> 2 <= 5 -> true

    if sum(s[i : j]) == d:
    sum(s[0 : 2]) == 4 -> sum(2 : 2) == 4 -> true
        count = count + 1
        count = 1

    i = i + 1
    i = 1
    j = j + 1
    j = 3

    -> 3 <= 5 -> true

    if sum(s[i : j]) == d:
    sum(s[1 : 3]) == 4 -> sum(2 : 1) -> false

    i = i + 1
    i = 2
    j = j + 1
    j = 4

    -> 4 <= 5 -> true

    if sum(s[i : j]) == d:
    sum(s[2 : 4]) == 4 -> sum(1 : 3) -> true
        count = count + 1
        count = 2

    i = i + 1
    i = 3
    j = j + 1
    j = 5

    -> 5 <= 5 -> true

    if sum(s[i : j]) == d:
    sum(s[3 : 5]) == 4 -> sum(3 : 5) -> false

    i = i + 1
    i = 4
    j = j + 1
    j = 6

    -> 6 <= 5 -> false

    return count 

    output = 2
'''