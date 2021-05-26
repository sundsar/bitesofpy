from datetime import date, timedelta


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    first_of_may = date(year, 5, 1)
    days_to_sunday = 7 - first_of_may.isoweekday()
    firstsunday_of_may = first_of_may + timedelta(days=days_to_sunday)
    return firstsunday_of_may + timedelta(days=7)
