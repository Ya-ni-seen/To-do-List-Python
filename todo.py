# Simple To-Do List App

tasks = []  # List to store tasks

def show_tasks():
    """Display the current tasks."""
    if not tasks:
        print("\n✅ No tasks yet!\n")
    else:
        print("\n📌 To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("\n")

def add_task():
    """Add a new task to the list."""
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"✅ Task '{task}' added!\n")

def remove_task():
    """Remove a task by number."""
    show_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"❌ Task '{removed}' removed!\n")
        else:
            print("⚠️ Invalid task number!\n")
    except ValueError:
        print("⚠️ Please enter a valid number!\n")

def main():
    """Main loop for the to-do list app."""
    while True:
        print("📝 To-Do List App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice, try again!\n")

if __name__ == "__main__":
    main()
