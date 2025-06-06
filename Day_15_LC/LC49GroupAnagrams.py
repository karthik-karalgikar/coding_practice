def groupAnagrams(strs):
    nums = []
    for i in range(len(strs)):
        a = list(strs[i])
        for j in strs[1:]:  
            if j in nums:
                continue
            b = list(j)


            if sorted(a) == sorted(b):
                if strs[i] in nums:
                    nums.append(j)
                else:
                    nums.extend([strs[i], j])

        if len(nums) == 0:
            nums.append(list(strs[i]))
        
    return nums

strs = ["eat","tea","tan","ate","nat","bat"]
result = groupAnagrams(strs)
print(result)