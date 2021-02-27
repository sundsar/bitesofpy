WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    row = int(size / 2)
    lst = [(WHITE, BLACK) * row if num % 2 == 0 else (BLACK, WHITE) * row
           for num in range(size)]
    for tpl in lst:
        print(*tpl, sep='')


create_chessboard()
