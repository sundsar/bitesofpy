from datetime import date
import re
from dateutil.relativedelta import relativedelta

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    tmp = re.findall('[0-9]{4}-[0-9]{2}-[0-9]{2}', data)
    return set([date.fromisoformat(d) for d in tmp])


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    dates = list(dates)
    dates.append(TODAY)
    lst = sorted(dates, reverse=True)
    streak = 0

    for idx, d in enumerate(lst):
        try:
            ndays = relativedelta(lst[idx], lst[idx + 1]).days
        except IndexError:
            return streak

        if ndays <= 1:
            streak += 1
        else:
            return streak
