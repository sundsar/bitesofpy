import csv
from collections import defaultdict
import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as s:
        download = s.get(CSV_URL)
        return download.content.decode('utf-8')


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    reader = csv.DictReader(content.splitlines())
    tz_info = defaultdict(int)
    for row in reader:
        tz_info[row['tz']] += 1
    for k in sorted(tz_info.keys()):
        plus_str = '+' * tz_info[k]
        print(f"{k:<20}| {plus_str}")
