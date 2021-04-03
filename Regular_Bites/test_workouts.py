import pytest

from workouts import print_workout_days


@pytest.mark.parametrize("workout, expected", [
    ('Upper', "Mon, Thu\n"),
    ('up', "Mon, Thu\n"),
    ('low', "Tue, Fri\n"),
    ('lower', "Tue, Fri\n"),
    ('body', "Mon, Tue, Thu, Fri\n"),
    ('car', "Wed\n"),
    ('cardo', "No matching workout\n"),
    ('min', "Wed\n"),
])
def test_print_workout_days(workout, expected, capsys):
    print_workout_days(workout)
    out, err = capsys.readouterr()
    assert out == expected
    assert err == ''
