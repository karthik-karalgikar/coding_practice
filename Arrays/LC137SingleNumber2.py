def singleNumber2(nums):
    frequency = {}
    for i in nums:
        if i in frequency:
            frequency[i] = frequency[i] + 1
        else:
            frequency[i] = 1
                
    for i in frequency:
        if frequency[i] != 3:
            return i
        
'''
TRACING - very easy, figure it out yourself
'''