import datetime
from pytz import timezone, utc

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    aware_utc_dt = naive_utc_dt.astimezone(timezone('UTC'))
    dt_aus = aware_utc_dt.astimezone(AUSTRALIA)
    dt_esp = aware_utc_dt.astimezone(SPAIN)
    return dt_aus, dt_esp


'''
def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    now_aware = utc.localize(naive_utc_dt)
    aus_dt = now_aware.astimezone(AUSTRALIA)
    es_dt = now_aware.astimezone(SPAIN)
    return aus_dt, es_dt

'''
