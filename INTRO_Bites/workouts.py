WORKOUT_SCHEDULE = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
REST, CHILL_OUT, TRAIN = 'Rest', 'Chill out!', 'Go train {}'
INVALID_DAY = 'Not a valid day'


def get_workout_motd(day):
    day = day.title()
    if day in WORKOUT_SCHEDULE:
        workout = WORKOUT_SCHEDULE[day]
        if workout == REST:
            return CHILL_OUT
        else:
            return TRAIN.format(workout)
    else:
        return INVALID_DAY
