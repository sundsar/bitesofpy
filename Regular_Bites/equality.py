from enum import Enum
from collections import Counter


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):
    if list1 is list2:
        res = Equality.SAME_REFERENCE
    elif list1 == list2:
        res = Equality.SAME_ORDERED
    elif sorted(list1) == sorted(list2):
        res = Equality.SAME_UNORDERED
    elif Counter(list1).keys() == Counter(list2).keys():
        res = Equality.SAME_UNORDERED_DEDUPED
    elif list1 != list2:
        res = Equality.NO_EQUALITY
    return res
