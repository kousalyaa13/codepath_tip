
def good_pairs(pile1, pile2, k):
    count = 0
    for i in pile1:
        for j in pile2:
            if i % (j * k) == 0:
                count += 1
    return count


pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))