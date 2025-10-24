def isSubsequence(s, t):
    # s = list(s)
    # t = list(t)
    i, j = 0, 0

    for j in range(len(t)):
        if i < len(s) and s[i] == t[j]:
            i = i + 1

    return i == len(s)

print(isSubsequence(s='abc', t='ahbgdc'))

'''
TRACING :

i = 0
j = 0

for j in range(len(t)):
len(t) = 5
j = 0 < 5 -> true

    -> j = 0

    if i < len(s) and s[i] == t[j]:
    0 < 3 -> true
    s[0] == t[0] -> a == a -> true

    i = i + 1 
    i = 1
    j = j + 1
    j = 1

    -> j = 1

    if i < len(s) and s[i] == t[j]:
    1 < 3 -> true
    s[1] == j[1] -> b == h -> false

    -> j = 2

    if i < len(s) and s[i] == t[j]:
    1 < 3 -> true
    s[1] == t[2] -> b == b -> true

    i = i + 1
    i = 2
    j = j + 1
    j = 3

    -> j = 3

    if i < len(s) and s[i] == t[j]:
    2 < 3 -> true
    s[2] == t[3] -> c == g -> false

    -> j = 4

    if i < len(s) and s[i] == t[j]:
    2 < 3 -> true
    s[2] == t[4] -> c == d -> false

    -> j = 5

    if i < len(s) and s[i] == t[j]:
    2 < 3 -> true
    s[2] == t[5] -> c == c -> true

    i = i + 1
    i = 3
    j = j + 1
    j = 6

out of range

if i = 3
len(s) = 3

Output = True
    

'''