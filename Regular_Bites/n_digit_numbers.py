from typing import List, TypeVar
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError
    result = list()
    for num in numbers:
        num = int(num * pow(10, (n - 1)))
        if len(str(num).strip('-')) > n:
            num = int(str(num)[:n])
        result.append(num)
    return result


print(n_digit_numbers([8, 9, 10], 2))
