def round_to_next(number: int, multiple: int):
    if number % multiple == 0:
        return number
    else:
        while True:
            if multiple < 0:
                number = number - 1
            else:
                number = number + 1
            if number % multiple == 0:
                return number
