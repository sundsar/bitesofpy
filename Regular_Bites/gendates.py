import datetime

PYBITES_BORN = datetime.datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates(dt=PYBITES_BORN):
    delta100 = datetime.timedelta(days=100)
    dt = PYBITES_BORN + delta100
    while True:
        yield dt
        dt += delta100


dt = gen_special_pybites_dates()
print(next(dt))

"""
>>> from itertools import islice
>>> from pprint import pprint as pp
>>> from gendates import gen_special_pybites_dates
>>> gen = gen_special_pybites_dates()
>>> pp(list(islice(gen, 5)))
[datetime.datetime(2017, 3, 29, 0, 0),
 datetime.datetime(2017, 7, 7, 0, 0),
 datetime.datetime(2017, 10, 15, 0, 0),
 datetime.datetime(2018, 1, 23, 0, 0),
 datetime.datetime(2018, 5, 3, 0, 0)]
"""
