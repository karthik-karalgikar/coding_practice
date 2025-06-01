def checkEqualPartitions(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        temp = []

        if 1 in nums:
            temp.append(1)
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] * nums[j] == target:
                    temp.extend([nums[i], nums[j]])
                
        print(nums.sort())
        if temp.sort() == sorted(nums):
            return True
        else:
            return False

nums = [3,1,6,4,2,4]
target = 24
result = checkEqualPartitions(nums, target)
print(result)