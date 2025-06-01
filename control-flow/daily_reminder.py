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

    # 4. Use a match-case statement to form the base reminder based on priority
    match priority:
        case "high":
            base_message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            base_message = f"Reminder: '{task}' is a medium priority task"
        case "low":
            base_message = f"Note: '{task}' is a low priority task"

    # 5. Modify the reminder if the task is time-bound
    if time_bound == "yes":
        # Append immediate-attention text for any priority
        base_message += " that requires immediate attention today!"
    else:
        # If not time-bound and low priority, suggest doing it when there’s free time
        if priority == "low":
            base_message += ". Consider completing it when you have free time."
        else:
            # For high or medium priority but not time-bound, just end with a period
            base_message += "."

    # 6. Print the final reminder
    print(base_message) # Corrected: Removed leading "\n"


if __name__ == "__main__":
    main()