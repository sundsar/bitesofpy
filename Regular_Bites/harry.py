import os
import urllib.request
import string
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')

urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    with open(stopwords_file, encoding='utf-8') as fhand:
        stopwords = fhand.read().splitlines()

    with open(harry_text, encoding='utf-8') as fhand:
        content = fhand.read().lower()
        content = content.translate(
            content.maketrans('', '', string.punctuation))

    words = content.split()
    c = Counter(words)
    for word in stopwords:
        if word in c:
            c.pop(word)
    return c.most_common()[0]
