def diagonal_sum(grid):
	total = 0
	n = len(grid)

	for i in range(n):
		# first diagonal is [i][i], [i+1][i+1], etc
		total += grid[i][i]
		total += grid[i][n - 1 - i]
	# if the total num of rows in odd, that means there a middle value to remove
	if n % 2 == 1: 
		total -= grid[n // 2][n // 2] # 3//2 = row 1 and col 1, subtracts num 5
	return total

grid = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
print(diagonal_sum(grid))

grid = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
print(diagonal_sum(grid))

grid = [
    [5]
]
print(diagonal_sum(grid))
