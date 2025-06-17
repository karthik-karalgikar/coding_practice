#similar to 2556

#here, we can't put any 0 at the beginning. only in the 2nd nunmber we can add 0

def maxDiff(self, num):
    numStr = str(num)

    replace_for_max = ''
    for i in numStr:
        if i != '9':
            replace_for_max = i
            break

    new_chars = []
    for i in numStr:
        if i == replace_for_max:
            new_chars.append('9')
        else:
            new_chars.append(i)
        
    max_str = ''.join(new_chars)

    min_str = numStr
    if numStr[0] != '1':
        min_str = numStr.replace(numStr[0], '1')
    else:
        for i in range(1, len(numStr)):
            if numStr[i] != '0' and numStr[i] != '1':
                min_str = numStr.replace(numStr[i], '0')
                break

            
    
        # new_chars2 = []
        # for i in numStr:
        #     if i == replace_for_min:
        #         new_chars2.append('1')
        #     else:
        #         new_chars2.append(i)
        
        # min_str = ''.join(new_chars2)

    return int(max_str) - int(min_str)