def running_sum(superhero_stats):
    for i in range(1, len(superhero_stats)):
        # replace the one you are on by adding the num before it
        superhero_stats[i]  += superhero_stats[i - 1]
    return(superhero_stats)

superhero_stats = [1, 2, 3, 4]
print(running_sum(superhero_stats))

superhero_stats = [1, 1, 1, 1, 1]
print(running_sum(superhero_stats))

superhero_stats = [3, 1, 2, 10, 1]
print(running_sum(superhero_stats))