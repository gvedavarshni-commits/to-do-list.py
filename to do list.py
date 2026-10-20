
# TODO APPLICATION

tasks = []
next_id = 1


def add_task():
    global next_id

    description = input("Enter task description: ").strip()

    if description == "":
        print("Task description cannot be empty!")
        return

    task = {
        "id": next_id,
        "description": description,
        "status": "Pending"
    }

    tasks.append(task)
    print("Task added successfully!")
    print("Task ID:", next_id)

    next_id += 1


def view_tasks():
    if len(tasks) == 0:
        print("No tasks found!")
    else:
        print("\n===== YOUR TASKS =====")

        for task in tasks:
            print("\nID:", task["id"])
            print("Task:", task["description"])
            print("Status:", task["status"])


def update_task():
    try:
        task_id = int(input("Enter task ID to update: "))

        for task in tasks:
            if task["id"] == task_id:
                new_description = input(
                    "Enter new task description: "
                ).strip()

                if new_description == "":
                    print("Task description cannot be empty!")
                    return

                task["description"] = new_description
                print("Task updated successfully!")
                return

        print("Error: Task ID not found!")

    except ValueError:
        print("Invalid input! Please enter a number.")


def complete_task():
    try:
        task_id = int(input("Enter task ID to complete: "))

        for task in tasks:
            if task["id"] == task_id:
                if task["status"] == "Completed":
                    print("Task is already completed!")
                else:
                    task["status"] = "Completed"
                    print("Task marked as completed!")
                return

        print("Error: Task ID not found!")

    except ValueError:
        print("Invalid input! Please enter a number.")


def delete_task():
    try:
        task_id = int(input("Enter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                print("Task deleted successfully!")
                return

        print("Error: Task ID not found!")

    except ValueError:
        print("Invalid input! Please enter a number.")


def main():
    while True:
        print("\n===== TODO APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_task()

            elif choice == 2:
                view_tasks()

            elif choice == 3:
                update_task()

            elif choice == 4:
                complete_task()

            elif choice == 5:
                delete_task()

            elif choice == 6:
                print("Thank you for using TODO Application!")
                break

            else:
                print("Invalid choice! Please select 1 to 6.")

        except ValueError:
            print("Invalid input! Please enter a number.")


main()
