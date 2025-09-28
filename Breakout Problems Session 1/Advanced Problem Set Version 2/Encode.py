def shuffle(message, indices):
	# list to store the shuffled characters with the length of message
	shuffled = [""] * len(message)
	
	for i in range(len(message)):
		# match the first num in indices with the corresponding indexed letter from message
		shuffled[indices[i]] = message[i]

    # join the list into a string and return it	
	return "".join(shuffled)


message = "evil"
indices = [3, 1, 2, 0]
print(shuffle(message, indices))

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
print(shuffle(message, indices))