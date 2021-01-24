import argparse
from functools import reduce


def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    if not numbers:
        raise SystemExit
    nums = [float(number) for number in numbers]
    if operation == 'add':
        res = reduce(lambda a, b: a + b, nums)
    elif operation == 'mul':
        res = reduce(lambda a, b: a * b, nums)
    elif operation == 'div':
        res = reduce(lambda a, b: a / b, nums)
    elif operation == 'sub':
        res = reduce(lambda a, b: a - b, nums)
    return round(res, 2)


def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = argparse.ArgumentParser(description='A simple calculator')
    parser.add_argument("-a", "--add", help='Sums numbers', nargs='*')
    parser.add_argument("-s", "--sub", help='Subtracts numbers', nargs='*')
    parser.add_argument("-m", "--mul", help='Multiplies numbers', nargs='*')
    parser.add_argument("-d", "--div", help='Divides numbers', nargs='*')
    return parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    call_calculator(stdout=True)
