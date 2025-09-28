def local_maximums(grid):
	n = len(grid)
	max_values = []
	for row in range(1, n - 1): # cause its a 3x3 grid, you have to do last row - 1 cause last row will never become the middle row
		max_in_row = []
		for col in range(1, n - 1): # same, last column will never become the middle column
			grid_max = max(
                grid[row - 1][col - 1], grid[row- 1][col], grid[row - 1][col + 1], # 9 9 8
				grid[row][col - 1], grid[row][col], grid[row][col + 1], # 5 6 2
				grid[row + 1][col - 1], grid[row + 1][col], grid[row + 1][col + 1], # 8 2 6
            )
			
            # alternative way to write this using list comprehension
			m = max(grid[row + dr][col + dc] for dr in (-1, 0, 1) for dc in (-1, 0, 1))
			
			max_in_row.append(grid_max)
		max_values.append(max_in_row)
	return max_values

grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
print(local_maximums(grid))

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
print(local_maximums(grid))

