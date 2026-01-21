from datetime import date, timedelta
from habit import Habit
from analytics import longest_streak

def test_longest_streak():
    habit = Habit("Exercise", "daily")
    habit.complete(date.today())
    habit.complete(date.today() + timedelta(days=1))
    habit.complete(date.today() + timedelta(days=2))

    assert longest_streak(habit) == 3
