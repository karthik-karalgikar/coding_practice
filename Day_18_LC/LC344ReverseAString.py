def reverseString(s):
    # s[:] = s[::-1]

    # return s

    a = []
    for i in s[::-1]:
        a.append(i)
    
    return a

s = ["h","e","l","l","o"]
print(reverseString(s))
