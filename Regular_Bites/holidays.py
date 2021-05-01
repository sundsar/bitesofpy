from collections import defaultdict
import os
from urllib.request import urlretrieve


from bs4 import BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, 'html.parser')
    for holiday_soup in soup.select('.list-table tbody tr'):
        # print('**', holiday_soup.prettify())
        month = holiday_soup('time')[0].text.split('-')[1]
        name = holiday_soup('a')[0].text.rstrip()
        holidays[month].append(name)
    return holidays


print(get_us_bank_holidays())
