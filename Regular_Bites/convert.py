def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    fmt = fmt.lower()
    if not isinstance(value, (int, float)):
        raise TypeError
    if fmt not in ('cm', 'in'):
        raise ValueError
    return round(value / 2.54, 4) if fmt == 'in' else round(value * 2.54, 4)
