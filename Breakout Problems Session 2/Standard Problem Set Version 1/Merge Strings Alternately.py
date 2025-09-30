def merge_alternately(word1, word2):
    merged = []
    # initialize pointers
    i = 0
    j = 0

    # while the length of the words are less than the pointers
    while i < len(word1) and j < len(word2):
        # keep alternatively merging
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1
    
    # if there are still leftover letters as 
    # the length is larger than the pointers
    if i < len(word1):
        # append the rest of the word
        merged.append(word1[i:])
    if j < len(word2):
        merged.append(word2[j:])

    return "".join(merged)
   
word1 = "wol"
word2 = "oze"
print(merge_alternately(word1, word2))

word1 = "hfa"
word2 = "eflump"
print(merge_alternately(word1, word2))

word1 = "eyre"
word2 = "eo"
print(merge_alternately(word1, word2))