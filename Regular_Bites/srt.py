from datetime import timedelta
from typing import List


def get_srt_section_ids(text: str) -> List[int]:
    """Parse a caption (srt) text passed in and return a
       list of section numbers ordered descending by
       highest speech speed
       (= ratio of "time past:characters spoken")

       e.g. this section:

       1
       00:00:00,000 --> 00:00:01,000
       let's code

       (10 chars in 1 second)

       has a higher ratio then:

       2
       00:00:00,000 --> 00:00:03,000
       code

       (4 chars in 3 seconds)

       You can ignore milliseconds for this exercise.
    """
    lst = text.strip().split('\n\n')
    res = []

    for snip in lst:
        num, tme, caption = snip.splitlines()
        tmp = tme.split(' --> ')
        h0, m0, s0 = tmp[0].split(',')[0].split(':')
        h1, m1, s1 = tmp[1].split(',')[0].split(':')
        time_past = timedelta(hours=int(h1), minutes=int(m1), seconds=int(
            s1)) - timedelta(hours=int(h0), minutes=int(m0), seconds=int(s0))
        chars = len(caption)
        rate = chars / time_past.total_seconds()
        res.append((int(num), rate))

    res = sorted(res, key=lambda x: x[1], reverse=True)

    return [item[0] for item in res]
