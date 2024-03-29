from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    lst = delay_time.split()

    days = 0
    seconds = 0
    minutes = 0
    hours = 0

    for s in lst:
        if s.endswith('d'):
            days = int(s[:-1])
        elif s.endswith('h'):
            hours = int(s[:-1])
        elif s.endswith('m'):
            minutes = int(s[:-1])
        elif s.endswith('s'):
            seconds = int(s[:-1])
        else:
            seconds = int(s)

    td = NOW + timedelta(days=days, hours=hours,
                         minutes=minutes, seconds=seconds)

    return f"{task} @ {td}"
