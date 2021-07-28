import requests
from collections import Counter

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off, multiply by 1,000 and return
         value as float"""
    cap = cap.replace('$', '')
    res = 0
    if cap.endswith('M'):
        cap = cap.strip('M')
        res = float(cap)
    elif cap.endswith('B'):
        cap = cap.strip('B')
        res = float(cap) * 1000
    return res


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    total_cap = 0
    for item in data:
        if item["industry"] == industry:
            cap = _cap_str_to_mln_float(item["cap"])
            total_cap += cap
    return round(total_cap, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    sorted_data = sorted(data, reverse=True,
                         key=lambda item: _cap_str_to_mln_float(item["cap"]))
    return sorted_data[0]["symbol"]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sec_sto = [item["sector"] for item in data if item["sector"] != "n/a"]
    c = Counter(sec_sto)
    lst = c.most_common()
    return lst[0][0], lst[-1][0]
