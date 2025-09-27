def highest_altitude(gain):
    highest = 0 # starts at 0, since point 0 has a max height of 0
    cumalative = 0
    
    for value in gain:
        cumalative += value
        # if cumalative value is higher than 0
        # then set it equal to highest
        if cumalative > highest:
            highest = cumalative

    return highest


gain = [-5, 1, 5, 0, -7]
print(highest_altitude(gain))

gain = [-4, -3, -2, -1, 4, 3, 2]
print(highest_altitude(gain))

gain = []
print(highest_altitude(gain))

gain = [0, 0, 0, 0]
print(highest_altitude(gain))

gain = [-1, -1, -1]
print(highest_altitude(gain))

# n is cumalative value
# 0, -5, -4, 1, 1, -6 - highest point here is 1
# 0, -4, -7, -9, -10, -6, -3, -1 - highest point is 0, initial value