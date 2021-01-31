from itertools import permutations, combinations


def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        return permutations(friends, team_size)
    return combinations(friends, team_size)


friends = 'Bob Dante Julian Martin'.split()
teams = list(friends_teams(friends, team_size=3, order_does_matter=True))
print(len(teams))
