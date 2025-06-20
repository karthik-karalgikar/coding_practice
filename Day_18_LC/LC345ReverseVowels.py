def reverseVowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    a = list(s)

    left = 0
    right = len(a) - 1

    while left < right:
        while left < right and a[left] not in vowels:
            left = left + 1
        while right > left and a[right] not in vowels:
            right = right - 1

        a[left], a[right] = a[right], a[left]

        left = left + 1
        right = right - 1

    return ''.join(a)

s = "IceCreAm"
print(reverseVowels(s))