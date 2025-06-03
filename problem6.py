def doubled(hunny_jars):
    doubled_list = []
    for num in hunny_jars:
        doubled_list.append(num * 2)
    return doubled_list

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))