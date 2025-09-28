def minimum_boxes(meals, capacity):
	total_meals = sum(meals)
	
    # sort capacities to get largest to smallest boxes to fill the least num of boxes
	capacity.sort(reverse = True)
	
	box_count = 0
	
	for cap in capacity:
		total_meals -= cap
		box_count += 1
		
        # if there are no more meals left to box
		if total_meals <= 0:
			return box_count

meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
print(minimum_boxes(meals, capacity))

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
print(minimum_boxes(meals, capacity))