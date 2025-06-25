def ReverseString2(s, k):
    n = len(s)
    res = ''

    for i in range(0, n, 2 * k):
        res = res + s[i: i + k][::-1] + s[i + k: i + 2 * k]

    return res

print(ReverseString2(s='abcdefg', k=2))

'''
TRACING :

s = "abcdefg"
k = 2

n = len(s) -> 7
n = 7

res = ''

for i in range(0, n, 2 * k):

    -> i = 0, till 7 and step size = 2 * k => 4

    res = res + s[i: i + k][::-1] + s[i + k: i + 2 * k]
    res = '' + s[0: 0 + 2][::-1] + s[0 + 2: 0 + 2 * 2]
    res = '' + s[0 : 2][::-1] + s[2 : 4]
    res = '' + 'ba' + 'cd'
    res = 'bacd'

    -> i = 4, till 7 and step size = 2 * k => 4

    res = res + s[i: i + k][::-1] + s[i + k: i + 2 * k]
    res = 'bacd' + s[4: 4 + 2][::-1] + s[4 + 2: 4 + 2 * 2]
    res = 'bacd' + s[4 : 6][::-1] + s[6 : 8]
    res = 'bacd' + 'fe' + 'g'
    res = 'bacdfeg'

    -> i = out of range

    res = 'bacdfeg'



'''