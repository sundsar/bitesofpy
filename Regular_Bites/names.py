NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    names = list(dict.fromkeys(names))
    return [name.title() for name in names]


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names, reverse=True, key=lambda a: a.split()[1])


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    firstnames = [name.split()[0] for name in names]
    return min(firstnames, key=len)


print(sort_by_surname_desc(dedup_and_title_case_names(NAMES)))
print(shortest_first_name(dedup_and_title_case_names(NAMES)))
