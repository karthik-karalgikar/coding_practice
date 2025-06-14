def minMaxDifference(num):
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

    replace_for_min = numStr[0]

    new_chars2 = []
    for i in numStr:
        if i == replace_for_min:
            new_chars2.append('0')
        else:
            new_chars2.append(i)

    min_str = ''.join(new_chars2)

    return int(max_str) - int(min_str)

num = 99
result = print(minMaxDifference(num))

'''
TRACING :

num = 11891

numStr = str(num)
=> numStr = '11891'

replace_for_max = ''

for i in numStr:
    => i = '1'
    if i != '9' -> '1' != '9' -> true
    replace_for_max = i 
    => replace_for_max = '1'
    break
    
new_chars = []

for i in numStr:
    i = '1'
    if i == replace_for_max: -> '1' == '1' -> true
        new_chars.append('9')
    
        new_chars = ['9']

    i = '1'
    if i == replace_for_max: -> '1' == '1' -> true
        new_chars.append('9')

        new_chars = ['9', '9']

    i = '8'
    if i == replace_for_max: -> '8' == '1' -> false
    else:
        new_chars.append(i) -> new_chars.append('8')

        new_chars = ['9', '9', '8']

    i = '9'
    if i == replace_for_max: -> '9' == '1' -> false
    else:
        new_chars.append(i) -> new_chars.append('9')

        new_chars = ['9', '9', '8', '9']

    i = '1'
    if i == replace_for_max: -> '1' == '1' -> true
        new_chars.append('9')

        new_chars = ['9', '9', '8', '9', '9]

max_str = ''.join(new_chars)
=> max_str = '99899'

replace_for_min = numStr[0]
=> replace_for_min = '1'

new_chars2 = []

for i in numStr:
    i = '1'
    if i == replace_for_min: -> '1' == '1' -> true
        new_chars2.append('0')

        new_chars2 = ['0']

    i = '1'
    if i == replace_for_min: -> '1' == '1' -> true
        new_chars2.append('0')

        new_chars2 = ['0', '0']

    i = '8'
    if i == replace_for_min: -> '8' == '1' -> false
    else:
        new_chars2.append('8')

        new_chars2 = ['0', '0', '8']

    i = '9'
    if i == replace_for_min: -> '9' == '1' -> false
    else:
        new_chars2.append('9')

        new_chars2 = ['0', '0', '8', '9']

    i = '1'
    if i == replace_for_min: -> '1' == '1' -> true
        new_chars2.append('0')

        new_chars2 = ['0', '0', '8', '9', '0']

min_str = ''.join(new_chars2)
=> min_str = '00890'

return int(max_str) - int(min_str)

int(max_str) = 99899
int(min_str) = 00890

int(max_str) - int(min_str)
99899 - 00890
= 99009

Output = 99009

'''