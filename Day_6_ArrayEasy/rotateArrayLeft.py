def rotate(nums, k):
       
    temp = []
   
    for i in range(len(nums) - k, len(nums)):
        temp.append(nums[i])

    for i in range(len(nums) - k):
        temp.append(nums[i])

    return temp

k = 3
nums = [1, 2, 3, 4, 5, 6, 7]
result = rotate(nums, k)
print(result)

'''
TRACING

temp = []
for loop, from 
len(nums) = 7 and k = 3, that is,
for loop will run from 4th index to 6th index(7 is the length of the list, but
7 is not included)
for i in range(4, 7):
    temp.append(nums[4])
    => temp = [5]
    temp.append(nums[5])
    => temp = [5,6]
    temp.append(nums[6])
    => temp = [5,6,7]

for the next for loop, it will run from 0 to 3rd index(4 is not included)
for i in range(0, 4):
    temp.append(nums[0])
    => temp = [5,6,7,1]
    temp.append(nums[1])
    => temp = [5,6,7,1,2]
    temp.append(nums[2])
    => temp = [5,6,7,1,2,3]
    temp.append(nums[3])
    => temp = [5,6,7,1,2,3,4]
    which is the expected output
    
'''