def get_item(items, x):
    if 0 <= x < len(items):
        print(items[x])
        return items[x]
    else:
        print(None)
        return None

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 4
get_item(items, x)