def goldilocks_approved(nums):
    maximum = max(nums)
    minimum = min(nums)
    
    if len(nums) <= 2:
        return -1

    for num in nums:
        if num != maximum and num != minimum:
            return num
    
    return -1


nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))