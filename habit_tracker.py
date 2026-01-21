from habit import Habit
from storage import save_habits, load_habits

class HabitTracker:
    def __init__(self, filename="habits.json"):
        self.filename = filename
        self.habits = load_habits(filename)

    def add_habit(self, name, periodicity):
        self.habits.append(Habit(name, periodicity))
        save_habits(self.habits, self.filename)

    def list_habits(self):
        return self.habits

    def get_habit(self, name):
        for h in self.habits:
            if h.name == name:
                return h
        return None
