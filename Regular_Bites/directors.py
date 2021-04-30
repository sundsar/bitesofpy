import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = os.getenv("TMP", "/tmp")


fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies_by_director = defaultdict(list)
    with open(MOVIE_DATA, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if len(row['director_name']) < 1 or len(row['movie_title']) < 1:
                continue
            if len(row['title_year']) < 1 or len(row['imdb_score']) < 1:
                continue
            if int(row['title_year']) < MIN_YEAR:
                continue
            director, title, year, score = row['director_name'], row['movie_title'], int(
                row['title_year']), float(row['imdb_score'])
            movies_by_director[director].append(Movie(title, year, score))
    return movies_by_director


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    return round(sum([nt.score for nt in movies]) / len(movies), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    lst = []
    for director, movies in directors.items():
        if len(movies) < MIN_MOVIES:
            continue
        lst.append((director, calc_mean_score(movies)))
    return(sorted(lst, key=lambda item: item[1], reverse=True))
