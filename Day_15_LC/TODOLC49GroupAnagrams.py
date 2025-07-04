# from type import List
import itertools

# def groupAnagrams(strs):
#     nums = []
#     for i in range(len(strs)):
#         a = list(strs[i])
#         for j in strs[1:]:  
#             if j in nums:
#                 continue
#             if strs[i] == j:
#                 continue
#             b = list(j)
            

#             if sorted(a) == sorted(b):
#                 if strs[i] in nums:
#                     nums.append(j)
#                 else:
#                     nums.extend([strs[i], j])

#         if len(nums) == 0:
#             nums.append(list(strs[i]))
        
#     return nums

# strs = ["eat","tea","tan","ate","nat","bat"]
# result = groupAnagrams(strs)
# print(result)

def groupAnagrams(strs):
    new_list = []
    for item in strs:
        new_list2 = []
        combinations = [''.join(p) for p in itertools.permutations(item)]

        for i in combinations:
            skip_this_loop = False
            for x in new_list:
                if i in x:
                    skip_this_loop = True
                    continue

            if skip_this_loop == True:
                continue

            for idx, z in enumerate(strs):
                if i in z:
                    new_list2.append(strs[idx])
                    break
        
        if new_list2:
            new_list.append(new_list2)

    return new_list

strs = ["",""]
print(groupAnagrams(strs))