import json
from habit import Habit

def save_habits(habits, filename):
    with open(filename, "w") as f:
        json.dump([h.to_dict() for h in habits], f, indent=2)

def load_habits(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Habit.from_dict(d) for d in data]
    except FileNotFoundError:
        return []
