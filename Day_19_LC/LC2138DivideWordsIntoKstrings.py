def divideString(s, k, fill):
    n = len(s)
    groups = (n + k - 1) // k
    result = []

    for i in range(groups):
        group = ''
        for j in range(k):
            index = i * k + j
            if index < n:
                group = group + s[index]
            else:
                group = group + fill
            
        result.append(group)

    return result

print(divideString(s='abcdefghih', k=3, fill='x'))