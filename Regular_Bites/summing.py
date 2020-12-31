def sum_numbers(numbers=None):
    if numbers is None:
        return sum(range(101))
    return sum(numbers)


print(sum_numbers())

'''
def sum_numbers(numbers=None):
    if numbers is None:
        numbers = range(1, 101)
    return sum(numbers)
    '''
