def MajElement(nums):
    freq = {}
    
    for i in nums:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1

    for i in freq:
        if freq[i] > len(nums) / 2:
            return i
        
    return False

print(MajElement(nums=[3,2,3]))

'''
TRACING :

same as 229
'''