def containsDuplicate(nums):
	return len(set(nums)) != len(nums)

nums = [1,2,3]
print(containsDuplicate(nums))


'''
TRACING:
nums = [1,1,2,3]

first convert the list into set by set(nums)
so then it will be {1,2,3}

and then we compare the length of the set and list
if it is the same, then there were no duplicates and it will return false
but if it was different, then it will know that there were duplicates and 
thus, the length is different. 
So it will return true.
'''
