import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

# prep
TMP = os.getenv("TMP", "/tmp")
tempfile = os.path.join(TMP, 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    data = ET.fromstring(content)
    categories = data.findall("channel/item/category")
    pytags = []
    for item in categories:
        pytags.append(item.text)
    c = Counter(pytags)
    return c.most_common(n)
