def ReverseString2(s, k):
    n = len(s)
    res = ''

    for i in range(0, n, 2 * k):
        res = res + s[i: i + k][::-1] + s[i + k: i + 2 * k]

    return res

print(ReverseString2(s='abcdefg', k=2))

