import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movie_list = []
    for file in files:
        with open(file) as f:
            contents = f.read()
        dct = json.loads(contents)
        movie_list.append(dct)
    return movie_list


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if 'Comedy' in movie['Genre']:
            return movie['Title']


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    dct = {}
    for movie in movies:
        title = movie['Title']
        _, nomstr = movie['Awards'].split('&')
        noms = int(nomstr.strip().split()[0])
        dct[title] = noms
    return sorted([(v, k) for k, v in dct.items()], reverse=True)[0][1]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    dct = {}
    for movie in movies:
        title = movie['Title']
        runtime = movie['Runtime'].replace(' min', '')
        dct[title] = int(runtime)
    return sorted([(v, k) for k, v in dct.items()], reverse=True)[0][1]
