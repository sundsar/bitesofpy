def remove_punctuation(input_string):
    import string
    return input_string.translate(input_string.maketrans('', '', string.punctuation))


print(remove_punctuation('''Hi !"#$%&\'There()*+,-'''))
