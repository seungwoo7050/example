tasks = []

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Update a Task")
    print("4. Remove a Task")
    print("5. Exit")

def add_task():
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"'{task}' has been added to the to-do list.")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def update_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to update: "))
        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the new description for the task: ")
            tasks[task_number - 1] = new_task
            print(f"Task {task_number} has been updated to '{new_task}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"'{removed_task}' has been removed from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
