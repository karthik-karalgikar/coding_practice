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