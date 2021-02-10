from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program
with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    automaker = []
    for item in data:
        if item["year"] == year:
            automaker.append(item.get("automaker"))
    return Counter(automaker).most_common()[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    models = set()
    for item in data:
        if item["automaker"] == automaker and item["year"] == year:
            models.add(item["model"])
    return models


print(most_prolific_automaker(2008))
print(get_models('Volkswagen', 2008))
