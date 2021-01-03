from collections import deque


def rotate(string, n):
    if not isinstance(string, str) or not isinstance(n, int):
        return
    d = deque(string)
    d.rotate(-n)
    return ''.join(d)


print(rotate('hello', 2))

'''
def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    return string[n:] + string[:n]

'''
