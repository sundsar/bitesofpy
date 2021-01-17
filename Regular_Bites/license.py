from string import ascii_uppercase, digits
from secrets import choice


def gen_key(parts=4, chars_per_part=8):
    chars = ascii_uppercase + digits
    combinations = [''.join(choice(chars)
                            for i in range(chars_per_part)) for i in range(parts)]
    return '-'.join(combinations)


print(gen_key())
print(gen_key(parts=3, chars_per_part=4))
print(gen_key(parts=10, chars_per_part=10))
