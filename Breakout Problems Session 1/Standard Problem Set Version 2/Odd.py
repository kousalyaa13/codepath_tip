def get_odds(nums):
    odd = []
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            odd.append(nums[i])
    return odd

nums = [1, 2, 3, 4]
print(get_odds(nums))

nums = [2, 4, 6, 8]
print(get_odds(nums))