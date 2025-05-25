'''
You are given two integer arrays nums1 and nums2, sorted in 
non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

'''

def merge(nums1, m, nums2, n):
    nums1 = nums1[:m]
    nums1.extend(nums2[:n])
    nums1.sort()
    return nums1

nums1 = [1]
m = 1 
nums2 = [] 
n = 0
result = merge(nums1, m, nums2, n)
print(result)

