import random
from functools import wraps

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        tries = MAX_RETRIES
        while tries > 0:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
            tries = tries - 1
        raise MaxRetriesException

    return wrapper


@retry
def get_two_numbers(numbers):
    """Give a list of items pick 2 random ones,
       if both are not ints raise a ValueError
    """
    chosen = random.sample(numbers, 2)
    if not all(type(i) == int for i in chosen):
        raise ValueError('not all ints')


get_two_numbers(['A', 'b'])
# get_two_numbers([1, 2, 3])
print(get_two_numbers.__doc__)
