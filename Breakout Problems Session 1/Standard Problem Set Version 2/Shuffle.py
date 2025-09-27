def shuffle(cards):
	shuffled = []
	halfsize = len(cards) // 2

	for i in range(halfsize):
		shuffled.append(cards[i])
		shuffled.append(cards[halfsize + i])
	return shuffled

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards))

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards))

cards = [10, 10, 2, 2]
print(shuffle(cards))