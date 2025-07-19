def remove_name(people, secret_identity):
	i = 0
	while i < len(people):
		if people[i] == secret_identity:
			people.pop(i)
			# if you don't want to change the
			# order and skip over values
			# use pop(i) as this removes the 
			# exact element and checks next element
			# without skipping over
		else:
			i += 1
    
    # for person in people:
	# 	if person == secret_identity:
	# 		people.remove(person)
	return people

people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
print(remove_name(people, secret_identity))

people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Spiderman'
print(remove_name(people, secret_identity))