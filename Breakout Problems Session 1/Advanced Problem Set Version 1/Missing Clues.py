
def find_missing_clues(clues, lower, upper):
   missing_ranges = []
   clues.sort() # sorts ascending

   # check the gap between the lower and first clue
   if lower < clues[0]:
       missing_ranges.append([lower, clues[0] - 1])

   for i in range(1, len(clues)):
       if clues[i - 1] + 1 < clues[i]:
           missing_ranges.append([clues[i - 1] + 1, clues[i] - 1])
   
   # check the gap between the last clue and upper
   if clues[-1] < upper:
       missing_ranges.append([clues[-1] + 1, upper])

   return missing_ranges
         

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))