from datetime import date

class Habit:
    def __init__(self, name: str, periodicity: str):
        self.name = name
        self.periodicity = periodicity  # "daily" or "weekly"
        self.completions = []

    def complete(self, completion_date: date):
        self.completions.append(completion_date)

    def to_dict(self):
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "completions": [d.isoformat() for d in self.completions],
        }

    @staticmethod
    def from_dict(data):
        h = Habit(data["name"], data["periodicity"])
        h.completions = [date.fromisoformat(d) for d in data["completions"]]
        return h
