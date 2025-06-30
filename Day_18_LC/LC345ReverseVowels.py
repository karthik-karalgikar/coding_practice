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

'''
TRACING :

s = "IceCreAm"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

a = ['I', 'c', 'e', 'C', 'r', 'e', 'A', 'm']

left = 0
right = len(a) - 1 = 7

while left <= right:
    -> true
    while left < right and a[left] not in vowels:
        0 < 7 -> true
        a[0] = 'I' not in vowels -> false
    
    while right > left and a[right] not in vowels:
        7 > 0 -> true
        a[7] = 'm' not in vowels -> true

        right = right - 1 -> 7 - 1
        right = 6
    
        6 > 0 -> true
        a[6] = 'A' not in vowels -> false

    a[left], a[right] = a[right], a[left]

    a[0] = a[6]
    a[6] = a[0]

    a = ['A', 'c', 'e', 'C', 'r', 'e', 'I', 'm'] 

    left = left + 1
    left = 1

    right = right - 1
    right = 5

    while left < right:
        1 < 5 -> true
        while left < right and a[left] not in vowels:
            1 < 5 -> true
            a[1] = 'c' not in vowels -> true
            
            left = left + 1
            left = 2

            2 < 5 -> true
            a[2] = 'e' not in vowels -> false

        while right > left and a[right] not in vowels:
            5 > 2 -> true
            a[5] = 'e' not in vowels -> false

            
        a[left], a[right] = a[right], a[left]

        a[2] = a[5]
        a[5] = a[2]

        a = ['A', 'c', 'e', 'C', 'r', 'e', 'I', 'm'] 

        left = left + 1
        left = 3

        right = right - 1
        right = 4

        while left < right:
            3 < 4 -> true
            while left < right and a[left] not in vowels:
                3 < 4 -> true
                a[3] = 'C' not in vowels -> true

                left = left + 1
                left = 4

                4 < 4 -> false
            
            while right > left and a[right] not in vowels: 
                4 > 4 -> false

        a[left], a[right] = a[right], a[left]

        a[4] = a[4]
        a[4] = a[4]

        left = left + 1
        left = 5

        right = right - 1
        right = 3

    while left < right:
        5 < 3 -> false

    return ''.join(a)

    Output = 'AceCreIm'

            

        



'''