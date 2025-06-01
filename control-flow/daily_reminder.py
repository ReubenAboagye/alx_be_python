# daily_reminder.py

def main():
    # 1. Prompt for a single task description
    task = input("Enter your task: ").strip()

    # 2. Prompt for the task’s priority and validate with a loop
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ("high", "medium", "low"):
            break
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

    # 3. Prompt for whether the task is time-bound (yes/no) and validate with a loop
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ("yes", "no"):
            break
        print("Invalid input. Please enter 'yes' or 'no'.")

    # 4. Use a match-case statement to handle each priority
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a medium priority task.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()
