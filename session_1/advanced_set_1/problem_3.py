def tiggerfy(word):
    # Convert to lowercase for matching, but keep original for output
    result = ""
    i = 0
    lower_word = word.lower()
    while i < len(word):
        # Check for "gg"
        if lower_word[i:i+2] == "gg":
            i += 2
        # Check for "er"
        elif lower_word[i:i+2] == "er":
            i += 2
        # Check for "t"
        elif lower_word[i] == "t":
            i += 1
        # Check for "i"
        elif lower_word[i] == "i":
            i += 1
        else:
            result += word[i]
            i += 1
    return result

word = "Trigger"
print(tiggerfy(word))  # Output: r

word = "eggplant"
print(tiggerfy(word))  # Output: egplan

word = "Choir"
print(tiggerfy(word))  # Output: Chor