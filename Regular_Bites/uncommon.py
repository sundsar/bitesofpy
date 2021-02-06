def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    # return len(set(my_cities).symmetric_difference(set(other_cities)))
    return len(set(my_cities) ^ set(other_cities))


my_cities = ['Rome', 'Paris', 'Madrid']
other_cities = ['Chicago', 'Seville', 'Berlin']
print(uncommon_cities(my_cities, other_cities))
