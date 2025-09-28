def hulk_smash(n):
	answer = []
	# need to start from 1 because: 0 % 3 = 0, and that prints "HulkSmash"
	for i in range(1, n + 1):
		if i % 3 == 0 and i % 5 == 0:
			answer.append("HulkSmash")
		elif i % 3 == 0:
			answer.append("Hulk")
		elif i % 5 == 0:
			answer.append("Smash")
		else:
			answer.append(str(i))
	return answer

n = 3
print(hulk_smash(n))

n = 5
print(hulk_smash(n))

n = 15
print(hulk_smash(n))