def minimum_boxes(meals, capacity):
	total_meals = sum(meals)
	
    # sort capacities to get largest to smallest boxes to fill the least num of boxes
	capacity.sort(reverse = True)
	
	num_boxes_used = 0
	current_cap = 0
	
	for cap in capacity:
		current_cap += cap
		num_boxes_used += 1
		
        # there is more current space than the total meals
		if current_cap >= total_meals:
			return num_boxes_used

meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
print(minimum_boxes(meals, capacity))

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
print(minimum_boxes(meals, capacity))