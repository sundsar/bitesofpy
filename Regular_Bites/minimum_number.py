from typing import List


def minimum_number(digits: List[int]) -> int:
    num = 0
    for digit in sorted(set(digits)):
        num = (num * 10) + digit
    return num
