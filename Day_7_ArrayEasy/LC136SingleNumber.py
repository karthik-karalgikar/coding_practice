'''
Given a non-empty array of integers nums, 
every element appears twice except for one. Find that single one.
'''

def singleNumber(nums):
    num_count = {}

    for num in nums:
        if num in num_count:
            num_count[num] = num_count[num] + 1
        else:
            num_count[num] = 1

    for num, count in num_count.items():
        if count == 1:
            return num

nums = [4,1,2,1,2]
print(singleNumber(nums))

'''
TRACING

nums = [4,1,2,1,2]

7 -> create an empty dictionary called num_count

now add items to dictionary. 
if that num is already present in the dictionary, then add it by 1
if it is not, then the value will be 1

for example:
    the first element is 4. 
    so the for loop will be:
    for 4 in nums:
        if 4 is in num_count (answer is no):
            so the dictionary will now be -> 4: 1
            that is, the key and value. key is 4 and value is the count, 
            which is 1

    next iteration:
    for 1 in nums:
        if 1 is in num_count (no):
            1 : 1

    for 2 in nums:
        if 2 is in num_count  (no):
            2 : 1

    for 1 in nums:
        if 1 is in num_count  (yes):
            1 : 2

    for 2 in nums:
        if 2 is in num_count (yes):
            2 : 2

    now for the next loop:
    for num, count in num_count.items()

    so items contains all the items in the dictionary:
    4 : 1, 1 : 2, 2 : 2
    like this
    so we are considering the num, which has the count as 1
    the key value pairs in this dictionaries are as follows:
    num : count
    so the num whose count is 1 is being returned. 
'''

def singleNumberMine(nums):
    freq = {}

    for i in nums:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
             freq[i] = 1

    for i in freq:
        if freq[i] == 1:
            return i
            
    return False

nums = [4,1,2,1,2]
print(singleNumberMine(nums))

'''
TRACING same as 169 and 229
'''
