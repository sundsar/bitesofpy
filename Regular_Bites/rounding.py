from math import ceil, floor


def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    if up:
        return [ceil(num) for num in transactions]
    return [floor(num) for num in transactions]


print(round_up_or_down([1.55, 9.17, 5.67, 6.77, 2.33, -2.05], False))
