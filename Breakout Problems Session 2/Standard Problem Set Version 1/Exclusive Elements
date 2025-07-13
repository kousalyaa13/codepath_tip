def exclusive_elemts(list1, list2):
	exclusive_list1 = []
	exclusive_list2 = []
	
	for word in list1:
		if word not in list2:
			exclusive_list1.append(word)
	
	for word in list2:
		if word not in list1:
			exclusive_list2.append(word)
	
	return exclusive_list1 + exclusive_list2

list1 = ["pooh", "roo", "piglet"]
list2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(list1, list2))

list1 = ["pooh", "roo"]
list2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elemts(list1, list2))

list1 = ["pooh", "roo", "piglet"]
list2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(list1, list2))