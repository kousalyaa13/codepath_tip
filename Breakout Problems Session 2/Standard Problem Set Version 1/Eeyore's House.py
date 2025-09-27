def good_pairs(pile1, pile2, k):
	good_count = 0
	
	for i in range(len(pile1)):
		for j in range(len(pile2)):
			if pile1[i] % (pile2[j] * k) == 0:
				good_count += 1
	return good_count

pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
# 1 % 1 = 0
# 3 % 1 = 0
# 3 % 3 = 0
# 4 % 1 = 0
# 4 % 4 = 0
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
# pile2 = [6, 12]
# 12 % 6 = 0
# 12 % 12 = 0
print(good_pairs(pile1, pile2, k))