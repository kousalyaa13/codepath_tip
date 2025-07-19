def common_elements(lst1, lst2):
    common = []

    for item1 in lst1:
        for item2 in lst2:
            if item1 == item2:
                common.append(item1)
    return common

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["super speed", "time travel", "dimensional travel"]
print(common_elements(lst1, lst2))

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["martial arts", "stealth", "master detective"]
print(common_elements(lst1, lst2))

lst1 = ["martial arts", "super strength", "master", "stealth", "super speed", "x-ray vision"]
lst2 = ["martial arts", "stealth", "master detective"]
print(common_elements(lst1, lst2))