def can_pair(item_quantities):
    for quantity in item_quantities:
        if quantity % 2 != 0:
            return False
    return True

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))  # True

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))  # False

item_quantities = []
print(can_pair(item_quantities))  # True
