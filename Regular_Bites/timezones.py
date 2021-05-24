import pytz

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    lst = []
    dt_aware = utc.replace(tzinfo=pytz.UTC)
    for tz in timezones:
        if tz not in TIMEZONES:
            raise ValueError
        lst.append(dt_aware.astimezone(
            pytz.timezone(tz)).hour in MEETING_HOURS)
    return all(lst)
