def left_right_difference(nums):
    n = len(nums)
    answer = [0] * n
    left_sum = [0] * n
    right_sum = [0] * n
    
    # calculate the left sum
    for i in range(1, n):
        left_sum[i] = left_sum[i - 1] + nums[i - 1]

    # calculate the right sum
    for i in range(n - 2, -1, -1):
        right_sum[i] = right_sum[i + 1] + nums[i + 1]

    # calculate the answer
    for i in range(n):
        answer[i] = left_sum[i] - right_sum[i]
    
    return answer

nums = [10, 4, 8, 3]
print(left_right_difference(nums))

nums = [1]
print(left_right_difference(nums))