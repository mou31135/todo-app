import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        try:
            tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
        return
    print("\nYour To-Do List:")
    print("-" * 30)
    for idx, task in enumerate(tasks, start=1):
        status = "✔️" if task['completed'] else "❌"
        print(f"{idx}. [{status}] {task['title']}")
    print("-" * 30)

def add_task(tasks):
    title = input("Enter the task description: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print(f"Task '{title}' added.")
    else:
        print("Task description cannot be empty.")

def mark_completed(tasks):
    display_tasks(tasks)
    try:
        choice = int(input("Enter the task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]['completed'] = True
            print(f"Task {choice} marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        choice = int(input("Enter the task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nSimple To-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
            save_tasks(tasks)
        elif choice == '4':
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
