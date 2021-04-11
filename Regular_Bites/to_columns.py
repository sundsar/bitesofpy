from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    lst = []
    for idx, name in enumerate(names, 1):
        lst.append(f"| {name:<10}")
        if idx % cols == 0:
            lst.append('\n')
    print(''.join(lst))
