
def harvest(vegetable_patch):
	count = 0
	for section in vegetable_patch:
		for letter in section:
			if letter == "c":
				count += 1
	return count

vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]
print(harvest(vegetable_patch))