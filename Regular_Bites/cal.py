def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    weekdays = dict()
    content = calendar_output.splitlines()
    days = content[1].split()
    for item in content[2:]:
        dates = [int(day) for day in item.split()]
        count = len(dates)
        if item.startswith(' '):
            weekdays.update(dict(zip(dates, days[-count:])))
        elif count == 7:
            weekdays.update(dict(zip(dates, days)))
        else:
            weekdays.update(dict(zip(dates, days[:count])))
    return weekdays
