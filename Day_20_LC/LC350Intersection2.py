def intersect(nums1, nums2):
    count = {}
    result = []

    if len(nums1) < len(nums2):
        for i in nums1:
            if i in count: 
                count[i] = count[i] + 1
            else:
                count[i] = 1
            
        for i in nums2:
            if i in count and count[i] > 0:
                result.append(i)
                count[i] = count[i] - 1

    else:
        for i in nums2:
            if i in count: 
                count[i] = count[i] + 1
            else:
                count[i] = 1
            
        for i in nums1:
            if i in count and count[i] > 0:
                result.append(i)
                count[i] = count[i] - 1

    return result

print(intersect(nums1 = [1,2,2,1], nums2 = [2,2]))

'''
TRACING : 

Here, we have to return all the elements which are common and not only one of them.

count = {}
result = []

nums1 = [1,2,2,1]
nums2 = [2,2]

if len(nums1) < len(nums2):
    4 < 2 -> false

else:
    for i in nums2:
        -> i = 2
        if i in count: -> count = {} -> false:
        else:
            count[2] = 1
            => count = {2 : 1}

        -> i = 2
        if i in count : -> count = {2 : 1} -> true:
            count[2] = count[2] + 1
            => count = {2 : 2}

    
    for i in nums1:
        i = 1
        if i in count and count[i] > 0:
            1 in count -> false
        
        i = 2
        if i in count and count[i] > 0:
            2 in count -> true
            count[2] = 2 -> 2 > 0 -> true

            result.append(2)
            result = [2]

            count[i] = count[i] - 1
            count[2] = 2 - 1
            count = {2 : 1}

        i = 2
        if i in count and count[i] > 0:
            2 in count -> true
            count[2] = 2 -> 2 > 0 -> true

            result.append(2)
            result = [2, 2]

            count[i] = count[i] - 1
            count[2] = 1 - 1
            count = {2 : 0}

        i = 1
        if i in count and count[i] > 0:
            1 in count -> false
        
result = [2, 2]


    
'''