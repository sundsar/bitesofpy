import os
from pathlib import Path
from urllib.request import urlretrieve
import xml.etree.ElementTree as ET
from collections import defaultdict


# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
        countries
    )

ns = {'wb': 'http://www.worldbank.org'}


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    incomes_cnames = defaultdict(list)
    tree = ET.parse(xml)
    root = tree.getroot()
    for country in root.findall("wb:country", ns):
        income_level = country.find('wb:incomeLevel', ns).text
        name = country.find('wb:name', ns).text
        incomes_cnames[income_level].append(name)
    return incomes_cnames
