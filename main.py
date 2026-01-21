from datetime import date
from habit_tracker import HabitTracker

def main():
    tracker = HabitTracker()

    print("Habit Tracker")
    print("1. Add habit")
    print("2. Complete habit")
    print("3. List habits")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Habit name: ")
        periodicity = input("Periodicity (daily/weekly): ")
        tracker.add_habit(name, periodicity)
        print("Habit added.")

    elif choice == "2":
        name = input("Habit name: ")
        habit = tracker.get_habit(name)
        if habit:
            habit.complete(date.today())
            print("Habit completed.")
        else:
            print("Habit not found.")

    elif choice == "3":
        for h in tracker.list_habits():
            print(f"- {h.name} ({h.periodicity})")

if __name__ == "__main__":
    main()
