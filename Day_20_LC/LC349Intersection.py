def intersection(nums1, nums2):
    # nums1 = set(nums1)
    # nums2 = set(nums2)

    
    return list(set(nums2) & set(nums1))
    
print(intersection(nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]))

'''
TRACING :

Bitwise &  = 
1 & 1 -> 1
0 & 1 -> 0
1 & 0 -> 0
0 & 0 -> 0

This gives us the common elements in an array/list

set(nums2) = {2}
set(nums1) = {1, 2}

set(nums2) & set(nums1) = {2}

list(set(nums2) & set(nums1)) = [2]

Output = [2]
 
'''