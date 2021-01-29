def get_index_different_char(chars):
    from string import ascii_letters, digits
    alphanumeric = ascii_letters + digits
    binarychars = [1 if item and str(
        item) in alphanumeric else 0 for item in chars]
    if binarychars.count(0) == 1:
        return binarychars.index(0)
    if binarychars.count(1) == 1:
        return binarychars.index(1)


print(get_index_different_char(list(range(1, 9)) + ['}'] + list('abcde')))
