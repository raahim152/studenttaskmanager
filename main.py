
from taskmanager import TaskManager


def display_menu():
    print("\n===== STUDENT TASK MANAGER =====")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def main():
    manager = TaskManager()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")

            try:
                task = manager.add_task(title)
                print(f"Task added successfully! ID: {task['id']}")

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            tasks = manager.display_tasks()

            if not tasks:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")

                for task in tasks:
                    status = "Completed" if task["completed"] else "Pending"

                    print(
                        f"ID: {task['id']} | "
                        f"Title: {task['title']} | "
                        f"Status: {status}"
                    )

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))

                if manager.complete_task(task_id):
                    print("Task marked as completed!")
                else:
                    print("Task not found.")

            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))

                if manager.delete_task(task_id):
                    print("Task deleted successfully!")
                else:
                    print("Task not found.")

            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "5":
            print("Thank you for using Student Task Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
