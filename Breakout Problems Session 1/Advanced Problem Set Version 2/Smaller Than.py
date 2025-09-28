def smaller_than_current(nums):
	# for each num in nums, count how many other nums are smaller than current num
    smaller_list = []

    for current in range(len(nums)):
        count = 0
        for i in range(len(nums)):
            if nums[current] > nums[i]:
                count += 1
        smaller_list.append(count)
    return smaller_list

nums = [8, 1, 2, 2, 3]
print(smaller_than_current(nums))

nums = [6, 5, 4, 8]
print(smaller_than_current(nums))

nums = [7, 7, 7, 7]
print(smaller_than_current(nums))