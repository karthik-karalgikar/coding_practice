def rotationCheck(s1, s2):
    if s1 == s2:
        return False
    
    s1List = list(s1)
    s2List = list(s2)

    for i in range(len(s1List)):
        s2List = [s2List[-1]] + s2List[:-1]
        if s2List == s1List:
            return True
        
    return False

'''
TRACING - Same as LC1752, but here have to convert string into list
'''

#Solution 2
def rotationCheck2(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return False
    
    return s2 in (s1 + s1)

'''
TRACING : 

s1 = "abcde"
s2 = "cdeab"

now, if we do s1 + s1 = "abcdeabcde"

so now we just have to check if s2 is present in the concatenation
'''