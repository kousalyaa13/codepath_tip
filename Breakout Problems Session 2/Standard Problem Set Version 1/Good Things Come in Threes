def make_divisible_by_3(nums):
    operation_count = 0
    for num in nums:
        if num % 3 == 1:
            operation_count += 1
            # 3 is divisible by 0
            # 1 - 1 = 0 % 3 = True
            # so only one operation
        if num % 3 == 2:
            operation_count += 1
    return operation_count

nums = [1, 2, 3, 4]
print(make_divisible_by_3(nums))

nums = [3, 6, 9]
print(make_divisible_by_3(nums))