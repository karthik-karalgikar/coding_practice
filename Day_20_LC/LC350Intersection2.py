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