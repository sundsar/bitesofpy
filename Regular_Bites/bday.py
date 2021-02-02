from datetime import date
# import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    # weekday = date.weekday()
    # return calendar.day_name[weekday]
    return date.strftime('%A')


feds_bday = date(1981, 8, 8)
print(weekday_of_birth_date(feds_bday))
