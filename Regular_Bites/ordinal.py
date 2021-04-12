ord_dict = {1: 'st', 2: 'nd', 3: 'rd'}


def get_ordinal_suffix(number):
    snum = str(number)
    if len(snum) > 1 and snum[-2] == '1':
        return snum + 'th'
    ordinal = ord_dict.get(number % 10, 'th')
    return snum + ordinal
