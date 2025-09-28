def wealthiest_customer(accounts):
	# max(sum of the row), compare, find index of largest
    index = 0
    max_wealth = 0

    for i in range(len(accounts)):
        total = sum(accounts[i]) # find individual sum of rows

        if total > max_wealth: # if the total sum value if bigger than the max
            max_wealth = total # make that value the new max
            index = i # keep track of the index
    return [index, max_wealth]

accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
print(wealthiest_customer(accounts))

accounts = [
	[1, 5],
	[7, 3],
	[3, 5]
]
print(wealthiest_customer(accounts))

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
print(wealthiest_customer(accounts))
