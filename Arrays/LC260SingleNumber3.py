def singleNumber3(nums):
    temp= []
    frequency = {}
    for i in nums:
        if i in frequency:
            frequency[i] = frequency[i] + 1
        else:
            frequency[i] = 1
                
    for i in frequency:
        if frequency[i] != 2:
            temp.append(i)

    return temp

'''
TRACING - very easy, figure it out yourself
'''