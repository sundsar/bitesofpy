from collections import Counter
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# # you can use this constant as key to the yyyymm:count dict
# YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    d = {}

    with open(commit_log) as f:
        for line in f.readlines():
            date_detail, file_log = linesine.split('|')
            _, dstr = date_detail.split("Date:")
            dobj = parse(dstr)

            if year and year != dobj.year:
                continue

            YEAR_MONTH = f"{dobj.year}-{dobj.month:02d}"

            flst = file_log.rstrip().split(',')
            flst.pop(0)
            clst = [int(item.lstrip().split()[0]) for item in flst]

            d[YEAR_MONTH] = d.get(YEAR_MONTH, 0) + sum(clst)

    c = Counter(d)
    return (c.most_common()[-1][0], c.most_common()[0][0])
