def pickingNumbers(arr):
    freq = {}

    for i in arr:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1

    max_len = 0

    for i in freq:
        max_len = max(max_len, freq[i] + freq.get(i + 1, 0))

    return max_len

print(pickingNumbers(arr = [1, 2, 2, 3, 1, 2]))

'''
TRACING - 

freq = {}

adding elements to dictionary -
freq = {1 : 2, 2 : 3, 3 : 1}

for i in freq:
    -> i = 1
    max_len = max(max_len, freq[i] + freq.get(i + 1, 0))
    max_len = max(0, freq[1] + freq.get(2, 0))
    max_len = max(0, 2 + 3)
    max_len = max(0, 5)
    max_len = 5

    -> i = 2
    max_len = max(max_len, freq[i] + freq.get(i + 1, 0))
    max_len = max(5, freq[2] + freq.get(2 + 1, 0))
    max_len = max(5, 3 + 1)
    max_len = max(5, 4)
    max_len = 5

    -> i = 3
    max_len = max(max_len, freq[i] + freq.get(i + 1, 0))
    max_len = max(5, 1 + 0)
    max_len = max(5, 1)
    max_len = 5

return max_len 

Output = 5
'''