from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapper(*args):
        for num in args:
            if not isinstance(num, int):
                raise TypeError
            if num < 0:
                raise ValueError
        return func(*args)
    return wrapper


@int_args
def sum_numbers(*numbers):
    return sum(numbers)


print(sum_numbers(1, 2, 3))
