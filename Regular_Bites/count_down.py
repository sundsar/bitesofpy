from functools import singledispatch


@singledispatch
def count_down(data_type):
    # TODO: Learn how to use singledispatch!
    raise ValueError


@count_down.register(float)
@count_down.register(int)
@count_down.register(str)
def _(arg):
    arg = str(arg)
    counter = len(arg)
    while counter > 0:
        print(arg[:counter])
        counter = counter - 1


@count_down.register(list)
@count_down.register(tuple)
@count_down.register(set)
@count_down.register(range)
@count_down.register(dict)
def _(arg):
    if isinstance(arg, dict):
        arg = list(arg.keys())
    strarg = ''
    for item in arg:
        strarg = strarg + str(item)
    counter = len(strarg)
    while counter > 0:
        print(strarg[:counter])
        counter = counter - 1
