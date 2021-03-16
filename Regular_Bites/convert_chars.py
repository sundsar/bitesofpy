PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    fromstr = PYBITES + 'PYBITES'
    tostr = fromstr.swapcase()
    return text.translate(text.maketrans(fromstr, tostr))
