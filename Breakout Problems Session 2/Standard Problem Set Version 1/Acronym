def is_acronym(words, s):
    if len(s) != len(words):
        return False

    acronym = ""
    for word in words:
        acronym += word[0]
    
    return s == acronym

words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))

words = ["christopher", "robin", "milne"]
s = "bs"
print(is_acronym(words, s))

words = ["christopher", "robin", "milne"]
s = "mrc"
print(is_acronym(words, s))

words = []
s = ""
print(is_acronym(words, s))