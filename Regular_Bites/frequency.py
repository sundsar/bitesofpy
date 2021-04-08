from collections import Counter


def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    c = Counter(numbers)
    items = c.most_common(len(c))
    major = items[0][0]
    minor = items[-1][0]
    return major, minor
