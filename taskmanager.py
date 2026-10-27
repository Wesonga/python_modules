
# Each task is stored in a dictionary with its completion status.
tasks = {}


def add_task(tasks, task):
    task = task.strip()

    if not task:
        return "Task cannot be empty."

    if task in tasks:
        return "Task already exists."

    tasks[task] = False
    return f"Task '{task}' added successfully."


def remove_task(tasks, task):
    task = task.strip()

    if task in tasks:
        del tasks[task]
        return f"Task '{task}' removed successfully."

    return "Task not found."


def view_tasks(tasks):
    if not tasks:
        return "Your to-do list is empty."

    output = ["\nYour To-Do List:"]

    for number, (task, completed) in enumerate(
        tasks.items(), start=1
    ):
        status = "Completed" if completed else "Pending"
        output.append(f"{number}. {task} - {status}")

    return "\n".join(output)


def complete_task(tasks, task):
    task = task.strip()

    if task not in tasks:
        return "Task not found."

    if tasks[task]:
        return "Task is already completed."

    tasks[task] = True
    return f"Task '{task}' marked as complete."


# User interface
while True:
    print("TO-DO LIST MANAGER")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Mark task as complete")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        task = input("Enter task to add: ")
        print(add_task(tasks, task))

    elif choice == "2":
        task = input("Enter task to remove: ")
        print(remove_task(tasks, task))

    elif choice == "3":
        print(view_tasks(tasks))

    elif choice == "4":
        task = input("Enter completed task: ")
        print(complete_task(tasks, task))

    elif choice == "5":
        print("Thank you for using the To-Do List Manager!")
        break

    else:
        print("Invalid choice. Please select 1-5.")
