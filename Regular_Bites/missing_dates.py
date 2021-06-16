from datetime import date
from dateutil.rrule import rrule, DAILY


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    given = sorted(dates)
    start_date, end_date = given[0], given[-1]
    tmp = list(rrule(DAILY, dtstart=start_date, until=end_date))
    full = [d.date() for d in tmp]
    return sorted(set(full) - set(given))


date_range = [date(year=2019, month=2, day=n) for n in range(1, 11, 2)]
print(get_missing_dates(date_range))
