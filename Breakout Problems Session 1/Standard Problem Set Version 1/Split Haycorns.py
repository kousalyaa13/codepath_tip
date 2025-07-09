
def split_haycorns(quantity):
    d_list = []

    for i in range(1, quantity + 1):
        if quantity % i == 0:
            d_list.append(i)

    return d_list

print(split_haycorns(6))
print(split_haycorns(13))
print(split_haycorns(1))