import re


def generate_affiliation_link(url):
    code = re.findall('dp/([A-Z0-9]+)', url)
    return f"http://www.amazon.com/dp/{code[0]}/?tag=pyb0f-20"


original_links = [
    ('https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/'
     '?keywords=war+of+art'),
    ('https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/'
     'ref=sr_1_1'),
    ('https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/'
     '?qid=1537226234'),
    'https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X',
    ('https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/'
     '1449340377/'),
    ('https://www.amazon.com/fake-book-with-longer-asin/dp/'
     '1449340377000/'),
]

for link in original_links:
    print(generate_affiliation_link(link))
