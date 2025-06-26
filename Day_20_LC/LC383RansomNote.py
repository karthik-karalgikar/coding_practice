def canConstruct(ransomNote, magazine):
    # countRansom = {}
    countMagazine = {}

    # for i in ransomNote:
    #     if i in count:
    #         count[i] = count[i] + 1
    #     else:
    #         count[i] = 1

    for i in magazine:
        if i in countMagazine:
            countMagazine[i] = countMagazine[i] + 1
        else:
            countMagazine[i] = 1

    for i in ransomNote:
        if i not in countMagazine:
            return False
        elif countMagazine[i] <= 0:
            return False
        else:
            countMagazine[i] = countMagazine[i] - 1

    return True

ransomNote = "cat"
magazine = "tac"
print(canConstruct(ransomNote, magazine))

'''
TRACING:

ransomNote = 'aa'
magazine = 'aab'

countMagazine = {}

for i in magazine: 
    -> i = 'a'
    if i in countMagazine:
        -> i = 'a', countMagazine = {} => false
    else:
        countMagazine[i] = 1 
        -> {'a' : 1}

    -> i = 'a'
    if i in countMagazine:
        -> i = 'a', countMagazine = {'a' : 1} -> true
        countMagazine[i] = countMagazine[i] + 1
        countMagazine = {'a' : 2}

    -> i = 'b'
    if i in countMagazine:
        -> i = 'b', countMagazine = {'a' : 2} -> false
    else:
        countMagazine[i] = 1
        countMagazine = {'a' : 2, 'b' : 1}

for i in ransomNote:
    -> i = 'a'
    if i not in countMagazine:
        countMagazine = {'a' : 2, 'b' : 1} -> false
    elif countMagazine[i] <= 0:
        countMagazine[a] = 2 -> false
    else:
        countMagazine[i] = countMagazine[i] - 1
        countMagazine = {'a': 1, 'b': 1}

    -> i = 'a'
    if i not in countMagazine: -> false
    
    elif countMagazine[i] <= 0: -> False

    else:
        countMagazine[i] = countMagazine[i] - 1
        countMagazine = {'a' : 0, 'b' : 1}

return True

'''

