def find_villain(crowd, villain):
    indexes = []
    for i in range(len(crowd)):
        if crowd[i] == villain:
            indexes.append(i)
    return indexes

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
print(find_villain(crowd, villain))