games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)

def print_game_stats(games_won):
    for k,v in games_won.items():
        if v == 1:
            print(k,'has won',v,'game')
        else:
            print(k,'has won',v,'games')

print_game_stats(games_won)