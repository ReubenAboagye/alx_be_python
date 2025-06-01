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

    # 4. Provide the customized reminder based on priority and time sensitivity
    if time_bound == "yes":
        # Any priority, but time-bound: immediate attention
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    else:
        # Not time-bound
        if priority == "low":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task.")

if __name__ == "__main__":
    main()
