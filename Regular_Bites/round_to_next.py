import math


def round_to_next(number: int, multiple: int):
    if math.remainder(number, multiple) == 0:
        return number
    else:
        while True:
            if number < 0 and multiple < 0:
                number = number - 1
            else:
                number = number + 1
            if math.remainder(number, multiple) == 0:
                return number


print(round_to_next(12_345, 42))
