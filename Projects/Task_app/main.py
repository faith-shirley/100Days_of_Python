"""
Main module for Todo application.

This module serves as the entry point and user interface for the Todo application.
It handles user interactions, delegates business operations to the appropriate use cases,
and displays results to the user. This module corresponds to the outermost layer in
Clean Architecture - the interface adapters and frameworks layer.
"""
from TodoRepository import InMemoryTodoRepository
from TodoUseCase import TodoUseCase


def main() -> None:
    """
    This function:
    1. Sets up the application's components (repository and use cases)
    2. Presents a menu-driven interface to the user
    3. Processes user commands and displays results
    4. Continues until the user chooses to exit

    The menu provides options to:
    - Add new tasks
    - List all tasks
    - Mark tasks as completed
    - Exit the application
    """

    repository = InMemoryTodoRepository()
    use_case = TodoUseCase(repository)

    next_id = 1

    # Main application loop
    while True:
        print("\n===== TODO LIST APPLICATION =====")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Add a new task workflow
            title = input("Enter task title: ")
            description = input("Enter task description: ")

            try:
                task = use_case.add_task(next_id, title, description)
                next_id += 1
                print(f"Task added: {task}")
            except ValueError as e:
                print(f"Error adding task: {str(e)}")

        elif choice == '2':
            # List all tasks workflow
            tasks = use_case.list_all_tasks()
            if tasks:
                print("\nAll Tasks:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks available.")

        elif choice == '3':
            # Mark task as completed workflow
            try:
                task_id = int(input("Enter task ID to mark as completed: "))

                try:
                    if use_case.mark_task_as_completed(task_id):
                        print(f"Task {task_id} marked as completed!")
                    else:
                        print(f"Task with ID {task_id} not found.")
                except ValueError as e:
                    print(f"Error: {str(e)}")

            except ValueError:
                print("Please enter a valid task ID (number).")

        elif choice == '4':
            # Exit the application
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()