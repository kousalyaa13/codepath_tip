def move_zeroes(lst):
    counter = 0
    result = []
    
    for num in lst:
        if num != 0:
            result.append(num)
        else:
            counter += 1

    for c in range(counter):
        result.append(0)
    
    return result

lst = [1, 0, 2, 0, 3, 0]
print(move_zeroes(lst))