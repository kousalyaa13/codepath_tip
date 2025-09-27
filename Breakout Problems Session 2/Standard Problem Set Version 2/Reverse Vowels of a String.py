def reverse_vowels(s):
    # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # instead of a list, use a set for faster lookup
    vowels = set('aeiouAEIOU')
    # convert the string to a list so that it can be editted
    # you cannot edit elements/letters of a string
    s = list(s)

    left = 0 # starts from left for string
    right = len(s) - 1 # starts from right of string

    while left < right: # so the two pointers don't overlap
        while left < right and s[left] not in vowels:
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1
        # swap the vowels
        # temp = s[left]
        # s[left] = s[right]
        # s[right] = s[left]

        # instead of using a temp variable
        # in one line you can swap
        s[left], s[right] = s[right], s[left]
        
        # keep going
        left += 1
        right -= 1

    return "".join(s)

s = "robin"
print(reverse_vowels(s))

s = "BATgirl"
print(reverse_vowels(s))

s = "batman"
print(reverse_vowels(s))

s = "calirole"
print(reverse_vowels(s))