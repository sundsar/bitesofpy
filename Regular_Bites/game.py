import csv
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
DATA = 'battle-table.csv'
BATTLE_DATA = os.path.join(TMP, DATA)
if not os.path.isfile(BATTLE_DATA):
    urlretrieve(
        f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
        BATTLE_DATA
    )


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    with open(BATTLE_DATA, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        defeat_mapping = dict.fromkeys(reader.fieldnames[1:])
        for row in reader:
            lst = [k for k, v in row.items() if v == 'win']
            defeat_mapping[row['Attacker']] = lst
        return defeat_mapping


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    players = list(defeat_mapping.keys())

    if player1 not in players or player2 not in players:
        raise ValueError

    if player1 == player2:
        return 'Tie'

    if player2 in defeat_mapping[player1]:
        return player1

    return player2
