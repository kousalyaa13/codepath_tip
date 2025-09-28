def defuse(code, k):
	result = []
	n = len(code)
	
	if k == 0:
		return [0] * n
	for i in range(n):
		total = 0
		if k > 0:
			# sum the next k numbers
			for j in range(1, abs(k) + 1):
				total += code[(i + j) % n]
			result.append(total)
		else:
			# sum the previous abs(k) numbers
			for j in range(1, abs(k) + 1):
				total += code[(i - j) % n]
			result.append(total)
	return result
						

code = [5, 7, 1, 4]
k = 3
print(defuse(code, k))

code = [1, 2, 3, 4]
k = 0
print(defuse(code, k))

code = [2, 4, 9, 3]
k = -2
print(defuse(code, k))