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

'''
TRACING:
 
s = 'abcdefghij'
k = 3
fill = 'x'

n = len(s) -> 'abcdefghij'
n = 10

groups = (n + k - 1) // k
groups = (10 + 3 - 1) // 3 -> 12 // 3
groups = 12

for i in range(groups): -> until 4
    -> i = 0
    group = ''
    for j in range(k):  
        -> j = 0, k = 3
        index = i * k + j -> 0 * 3 + 0
        index = 0
        if index < n: -> 0 < 10 => true
            group = group + s[index] -> '' + s[0]
            group = '' + 'a'
            group = 'a'

        -> j = 1, k = 3
        index = i * k + j -> 0 * 3 + 1
        index = 1
        if index < n: -> 1 < 10 => true
            group = group + s[index] -> 'a' + s[1]
            group = 'a' + 'b'
            group = 'ab'

        -> j = 2, k = 3
        index = i * k + j -> 0 * 3 + 2
        index = 2
        if index < n: -> 2 < 10 => true
            group = group + s[index] -> 'ab' + s[2]
            group = 'ab' + 'c'
            group = 'abc'

        -> j = 3, k = 3 -> out of range

    result.append(group)
    result.append('abc')

    => result = ['abc']

for i in range(groups):
    -> i = 1
    group = ''
    for j in range(k):
        -> j = 0, k = 3
        index = i * k + j -> 1 * 3 + 0
        index = 3
        if index < n: -> 3 < 10 => true
            group = group + s[index]
            group = '' + 'd'
            group = 'd'

        -> j = 1, k = 3
        index = i * k + j -> 1 * 3 + 1
        index = 4
        if index < n: -> 4 < 10 => true
            group = group + s[index]
            group = 'd' + 'e'
            group = 'de'

        -> j = 2, k = 3
        index = i * k + j -> 1 * 3 + 2
        index = 5
        if index < n: -> 5 < 10 => true
            group = group + s[index]
            group = 'de' + 'f'
            group = 'def'

        -> j = 3, k = 3 -> out of range

    result.append(group)
    result.append('def')

    => result = ['abc', 'def']

for i in range(groups):
    -> i = 2
    group = ''
    for j in range(k):
        -> j = 0, k = 3
        index = i * k + j -> 2 * 3 + 0
        index = 6
        if index < n: -> 6 < 10 => true
            group = group + s[index]
            group = '' + 'g'
            group = 'g'

        -> j = 1, k = 3
        index = i * k + j -> 2 * 3 + 1
        index = 7
        if index < n: -> 7 < 10 => true
            group = group + s[index]
            group = 'g' + 'h'
            group = 'gh'

        -> j = 2, k = 3
        index = i * k + j -> 2 * 3 + 2
        index = 8
        if index < n: -> 8 < 10 => true
            group = group + s[index]
            group = 'gh' + 'i'
            group = 'ghi'

        -> j = 3, k = 3 -> out of range
    
    result.append(group)
    result.append('ghi')

    result = ['abc', 'def', 'ghi']

for i in range(groups):
    -> i = 3
    group = ''
    for j in range(k):
        -> j = 0, k = 3
        index = i * k + j -> 3 * 3 + 0
        index = 9
        if index < n: 9 < 10 => true
            group = group + s[index]
            group = '' + 'h'
            group = 'h'

        -> j = 1, k = 3
        index = i * k + j -> 3 * 3 + 1
        index = 10
        if index < n: 10 < 10 => false
        else:
            group = group + fill
            group = 'h' + 'x'
            group = 'hx'

        -> j = 2, k = 3
        index = i * k + j -> 3 * 3 + 2
        index = 11
        if index < n: 11 < 10 => false
        else:
            group = group + fill
            group = 'hx' + 'x'
            group = 'hxx'

        -> j = 3, k = 3 -> out of range

    result.append(group)
    result.append('hxx') 

    result = ['abc', 'def', 'ghi', 'hxx']

for i in range(groups): 
-> i = 4, groups = 4 -> out of range

return result

Output = ['abc', 'def', 'ghi', 'hxx']


        

'''