from datetime import timedelta

def longest_streak(habit):
    if not habit.completions:
        return 0

    dates = sorted(habit.completions)
    streak = 1
    longest = 1

    for i in range(1, len(dates)):
        if dates[i] - dates[i - 1] == timedelta(days=1):
            streak += 1
        else:
            streak = 1
        longest = max(longest, streak)

    return longest
