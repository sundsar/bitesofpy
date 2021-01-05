def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    return len(text) - len(text.lstrip(' '))


print(count_indents('\tstr  '))
print(count_indents('    string'))
