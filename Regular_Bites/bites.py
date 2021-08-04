import csv
import os
from pathlib import Path
from urllib.request import urlretrieve
from operator import itemgetter

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        lst = []
        for row in reader:
            if row['Difficulty'].isalpha():
                continue
            bite_num = row['Bite'].split('.')[0].replace('Bite ', '')
            level = float(row['Difficulty'])
            lst.append((bite_num, level))
        res = sorted(lst, reverse=True, key=lambda tpl: tpl[1])[:N]
        return [tpl[0] for tpl in res]


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)
