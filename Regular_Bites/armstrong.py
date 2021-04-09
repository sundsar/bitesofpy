def is_armstrong(n: int) -> bool:
    # your code ...
    str_num = str(n)
    digits = len(str_num)
    total = 0
    for i in str_num:
        total += pow(int(i), digits)
    return n == total
