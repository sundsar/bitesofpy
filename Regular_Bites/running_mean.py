from itertools import accumulate


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    for idx, v in enumerate(accumulate(sequence), 1):
        yield round(v / idx, 2)


x = running_mean([1, 2, 3])
print(next(x))
print(next(x))
print(next(x))
