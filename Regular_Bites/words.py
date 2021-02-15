def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    dlst = [word for word in words if word[0] in '0123456789']
    clst = [word for word in words if word[0] not in '0123456789']
    return sorted(clst, key=lambda s: s.lower()) + sorted(dlst)


words = ("Andrew Carnegie's 64-room chateau at 2 East 91st "
         "Street was converted into the Cooper-Hewitt National "
         "Design Museum of the Smithsonian Institution "
         "in the 1970's").split()

print(sort_words_case_insensitively(words))
