def maximumProduct(nums):
       
    max_product = float("-inf")

    numsSort = sorted(nums)
    # for i in range(len(nums) - 2):
    #     for j in range(1, len(nums)):
    prod1 = numsSort[-1] * numsSort[-2] * numsSort[-3]
    prod2 = numsSort[0] * numsSort[1] * numsSort[-1]
    max_product = max(prod1, prod2)

    return max_product

nums = [-100, -2, -3, 1]
print(maximumProduct(nums))