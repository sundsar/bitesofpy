import xml.etree.ElementTree as ET

# from OMDB
xmlstring = '''<?xml version="1.0" encoding="UTF-8"?>
<root response="True">
  <movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
  <movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
  <movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
  <movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
  <movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
</root>'''  # noqa E501


def get_tree(str1=xmlstring):
    tree = ET.fromstring(xmlstring)
    return tree


def get_movies():
    tree = get_tree()
    lst = []
    for movie in tree.findall('movie'):
        lst.append(movie.get('title'))
    return lst


def get_movie_longest_runtime():
    tree = get_tree()
    lst = []
    for movie in tree.findall('movie'):
        title, runtime = movie.get('title'), movie.get('runtime')
        lst.append((title, runtime))
    sortedlst = sorted(lst, key=lambda a: a[1].split(), reverse=True)
    return sortedlst[0][0]


# print(get_tree())
# print(get_movies())
print(get_movie_longest_runtime())
