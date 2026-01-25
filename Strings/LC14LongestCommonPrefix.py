def longestCommonPrefix(strs):
    result = []
    strs.sort()
  

    if len(strs) > 0:
        first = strs[0]
        last = strs[-1]
        for i in range(len(first)):
            if last[i] == first[i]:
                result.append(last[i])
            else:
                return ''.join(result)
            
    return ''.join(result)

'''
TRACING - 
strs = ["flower","flow","flight"]
strs.sort() -> ["flight", "flow", "flower"]
first = strs[0] -> flight
last = strs[-1] -> flower

len(first) = 6
len(last) = 6

if last[i] == first[i]:
    f == f -> true
    result.append(last[i]) -> result = ['f']

    l == l -> true
    result.append(last[i]) -> result = ['f', 'l']

    i == o -> false

    else:
        return ''.join(result) -> 'fl'
'''
            

        
