from csv import DictReader
import os
from urllib.request import urlretrieve
from collections import Counter, defaultdict

TMP = os.getenv("TMP", "/tmp")
LOGS = 'bite_output_log.txt'
DATA = os.path.join(TMP, LOGS)
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com'
if not os.path.isfile(DATA):
    urlretrieve(f'{S3}/{LOGS}', DATA)


class BiteStats:

    def _load_data(self, data) -> list:
        with open(data, encoding="utf-8") as csvfile:
            reader = DictReader(csvfile)
            return [row for row in reader]

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        unique_bites = defaultdict(int)
        for row in self.rows:
            bite_num = row['bite']
            unique_bites[bite_num] += 1
        return len(unique_bites)

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        unique_bitesres = defaultdict(int)
        for row in self.rows:
            if row['completed'] != 'True':
                continue
            bite_num = row['bite']
            unique_bitesres[bite_num] += 1
        return len(unique_bitesres)

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        unique_users = defaultdict(int)
        for row in self.rows:
            user = row['user']
            unique_users[user] += 1
        return len(unique_users)

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        unique_usersres = defaultdict(int)
        for row in self.rows:
            if row['completed'] != 'True':
                continue
            user = row['user']
            unique_usersres[user] += 1
        return len(unique_usersres)

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        lst = [row['bite'] for row in self.rows]
        return Counter(lst).most_common()[0][0]

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        unique_usersres = defaultdict(int)
        for row in self.rows:
            if row['completed'] != 'True':
                continue
            user = row['user']
            unique_usersres[user] += 1
        return sorted(unique_usersres, reverse=True, key=lambda k: unique_usersres[k])[0]
