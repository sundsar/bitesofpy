from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    lst = [set(arg) for arg in args if arg]
    if not lst:
        return set()
    return set.intersection(*lst)
