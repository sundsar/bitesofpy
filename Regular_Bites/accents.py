from string import printable


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    text = text.lower()
    letters = set(text.translate(text.maketrans('', '', printable)))
    return letters
