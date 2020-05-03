def divide_numbers(numerator, denominator):
    try:
        n = int(numerator)
        d = int(denominator)
    except:
        raise ValueError

    try:
        return n/d
    except ZeroDivisionError:
        return 0