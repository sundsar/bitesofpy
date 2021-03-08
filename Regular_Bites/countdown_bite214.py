def countdown():
    """Write a generator that counts from 100 to 1"""
    for num in reversed(range(1, 101)):
        yield num
