scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()


def get_belt(user_score):
    d = dict(zip(scores, belts))
    for score in reversed(d):
        if user_score >= score:
            return d[score]


print(get_belt(0))
