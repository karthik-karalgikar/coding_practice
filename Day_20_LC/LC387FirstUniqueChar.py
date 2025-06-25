def firstUniqChar(s):
    a = set()
    for i in range(0, len(s)):
        if s[i] not in a and s.count(s[i]) == 1:
            return i
        elif s[i] not in a:
            a.add(s[i])
    return -1

print(firstUniqChar(s='aabb'))

'''
TRACING :

s = 'leetcode'

a = set()
a = {}

for i in range(0, len(s)):
    -> i = 0, len(s) = 8
    if s[i] not in a and s.count(s[i]) == 1:    
        s[i] = s[0] = l
        l not in a -> true

        s.count(s[i]) == 1 -> true

        return i -> 0

Output = 0

NOTE - s.count(s[i]) checks the whole list in the backend and then gives us the answer without us traversing through the
whole list
This can take a lot of time if the list is huge. 
So, dictionaries can be used.
'''

#Solution 2 :

def firstUniqueChar(s):
    frequency = {}

    for i in s:
        if i in frequency:
            frequency[i] = frequency[i] + 1
        else:
            frequency[i] = 1

    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i
        
    return -1

print(firstUniqueChar(s='aabb'))


