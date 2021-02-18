from collections import Counter


def freq_digit(num: int) -> int:
    return int(Counter(str(num)).most_common(1)[0][0])


print(freq_digit(748791789189717891789))
