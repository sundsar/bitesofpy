from collections import Counter
from contextlib import contextmanager
from datetime import date
from time import time

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = Counter()

def get_today():
    """Making it easier to test/mock"""
    return date.today()


@contextmanager
def timeit():
    startdate = get_today()
    start = time()
    try:
        yield
    finally:
        end = time() - start
        if end >= OPERATION_THRESHOLD_IN_SECONDS:
            violations[startdate] = violations.get(startdate, 0) + 1
        if violations[startdate] >= ALERT_THRESHOLD:
            print(ALERT_MSG)




