# index all letters in s, and if they match t i g e r, remove it

def tiggerfy(s):
	# letters that need to be removed
	remove_letters = "tiger"
	# new result after unneeded letters are removed
	result = ""

    # for each letter in string
	for letter in s:
		# lower the letter first, then if its not one of the bad letters
		if letter.lower() not in remove_letters:
			# add it to the new resulting word
			result += letter
	return result

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))
