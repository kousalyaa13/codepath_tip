def words_with_char(words, x):
	indexes = []
	for i in range(len(words)): # individual words
		if x in words[i]: # if x in the individual letters of the word
			indexes.append(i)
	return indexes				

words = ["batman", "superman"]
x = "a"
print(words_with_char(words, x))

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
print(words_with_char(words, x))

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
print(words_with_char(words, x))