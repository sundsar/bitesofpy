from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    d = feedparser.parse(FEED_URL)
    lst = []
    for entry in d['entries']:
        lst.append(Game(entry['title'], entry['link']))
    return lst


games = get_games()
print(games)
print(games[0])
print(games[-1])
