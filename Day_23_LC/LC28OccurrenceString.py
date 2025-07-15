def strStr(haystack, needle):
    if len(haystack) < len(needle):
        return -1
    
    for i in range(len(haystack)):
        if haystack[i : i + len(needle)] == needle:
            return i
        
    return -1


print(strStr(haystack="sadbutsad", needle="sad"))

'''
TRACING : 

haystack = "sadbutsad"
needle = "sad"

len(haystack) = 9
len(needle) = 3

if len(haystack) < len(needle):
    9 < 3 -> false

for i in range(len(haystack)):
    -> i = 0, until 9
    if haystack[0 : 0 + 3] == "sad"
    if haystack[0 : 3] == "sad"
    haystack[0 : 3] = "sad"

    "sad" == "sad"

    return i 

    Output = 0
 
'''