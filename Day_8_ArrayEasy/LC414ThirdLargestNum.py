'''
Given an integer array nums, return the third distinct maximum number 
in this array. 
If the third maximum does not exist, return the maximum number.
'''

def thirdMax(nums):
    numSet = set(nums)
    n = len(set(nums))
    if n == 0 or n == 1 or n == 2:
        return max(numSet)
    sortednumSet = sorted(numSet)
    thirdLarge = sortednumSet[n - 3]
    return thirdLarge 

nums = [1,1,3]
result = thirdMax(nums)
print(result)

'''
TRACING
nums = [1,1,2,3]
First, convert the list into set so as to remove all the duplicates
so numSet becomes = {1,2,3}
n = length of the set
now check if the length of the set is 0, 1 or 2
If it is not then sort he set. 
Note: for sets we just can't write numSet.sort() like we do with lists.
so initialize sortednumSet as the new sorted set. 
now the third largest number will be the third number from the last, that is,
n - 3
so in this case:
thirdLarge = sortednumSet[n - 3]
which means, thirdLarge = sortednumSet[3-3] => sortednumSet[0] => 1
so the third larget number is 1

Testcase 2:
nums = [1,1,2]
convert into set -> {1,2}
n = 2
so here the if condition is true. Therefore, the max of the numSet is returned
that is, the max of {1,2} is 2


'''