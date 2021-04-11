from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if len(lst_of_lst) < 1:
        return
    res = []
    for lst in lst_of_lst:
        res.extend((lst + list(sep)))
    return res[:-1]
