def non_decreasing(nums):
	count = 0
	
	for i in range(len(nums) - 1):
		# if current num is greater than the next num, add to count to return False
		if nums[i] > nums[i + 1]:
			count += 1
		
        # if the count if 0, return False
		if count > 1:
			return False
		
        # if before num is less than after num, 
        # you can make the current num equal the after num
		# ex: [2, 4, 3] --> [2, 3, 3]
		if i == 0 or nums[i - 1] <= nums[i + 1]:
			nums[i] = nums[i + 1]
			
		# if lowering current num doesn't work because it messes up the after
		# ex: [5, 7, 4]
		# you can make 4 --> 7
		# this makes [5, 7, 7]
		else:
			# after num = current num
			nums[i + 1] = nums[i]
	return True
						
nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))

nums = [4, 1, 2, 3, 5]
print(non_decreasing(nums))
