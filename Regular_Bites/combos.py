from itertools import combinations


def find_number_pairs(numbers, N=10):
    return [tpl for tpl in combinations(numbers, 2) if sum(tpl) == N]


print(find_number_pairs([-9, 29, 11, 10, 9, 3, -1, 21], 20))
