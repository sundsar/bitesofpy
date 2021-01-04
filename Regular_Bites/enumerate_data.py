def enumerate_names_countries():
    lst = zip(names, countries)
    for idx, (name, country) in enumerate(lst, start=1):
        name = name + (' ' * (11 - len(name)))
        fstr = "{}. {}{}"
        print(fstr.format(idx, name, country))


"""
def enumerate_names_countries1():
    fmt = '{}. {:<10} {}'
    for i, (name, country) in enumerate(zip(names, countries), 1):
        print(fmt.format(i, name, country))

"""


names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()

enumerate_names_countries()
