from datetime import timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(
    os.getenv("TMP", "/tmp"),
    'course_timings'
)

urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
    COURSE_TIMES
)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    timestamp = re.compile(r"\(([0-9:]+)")
    with open(COURSE_TIMES) as f:
        return timestamp.findall(f.read())


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    tdelta = timedelta()
    for timestamp in timestamps:
        mi, se = timestamp.split(':')
        td = timedelta(minutes=int(mi), seconds=int(se))
        tdelta = tdelta + td
    return str(tdelta)
