def delete_minimum_elements(hunny_jar_sizes):
    sorted = []
    while hunny_jar_sizes:
        minimum = min(hunny_jar_sizes)
        sorted.append(minimum)
        hunny_jar_sizes.remove(minimum)

    return sorted

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [2, 2, 2, 2]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = []
print(delete_minimum_elements(hunny_jar_sizes))