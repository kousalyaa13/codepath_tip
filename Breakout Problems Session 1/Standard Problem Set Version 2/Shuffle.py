def shuffle(cards):
    new = []
    half = len(cards)//2
    for i in range(half):
        new.append(cards[i]) # return first
        new.append(cards[i + half]) # return first after half mark
    return new
cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards))

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards))

cards = [10, 10, 2, 2]
print(shuffle(cards))