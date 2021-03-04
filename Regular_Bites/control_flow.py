IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    lst = []
    for name in names:
        if name.startswith(IGNORE_CHAR):
            continue
        elif not name.isalpha():
            continue
        elif name.startswith(QUIT_CHAR):
            break
        else:
            lst.append(name)
    return lst[:MAX_NAMES]


print(filter_names(['t2im', '1quinton', 'a3na', '4']))
