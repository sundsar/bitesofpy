import datetime


def tomorrow(asof=None):
    if asof is None:
        asof = datetime.date.today()
    return asof + datetime.timedelta(days=1)
