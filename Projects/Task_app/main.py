"""
Main application module for Todo application.
This module serves as the entry point and user interface.
"""

from TodoRepository import InMemoryTodoRepository
from TodoUseCase import TodoUseCase

def main():
    """
    This function initializes the necessary components, then provides
    a simple terminal-based interface for interacting with the application.
    """
    # Initialize the repository and use case
    repository = InMemoryTodoRepository()
    use_case = TodoUseCase(repository)

    # Track the next available ID
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
            # Add a new task
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = use_case.add_task(next_id, title, description)
            next_id += 1
            print(f"Task added: {task}")

        elif choice == '2':
            # List all tasks
            tasks = use_case.list_all_tasks()
            if tasks:
                print("\nAll Tasks:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks available.")

        elif choice == '3':
            # Mark a task as completed
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                if use_case.mark_task_as_completed(task_id):
                    print(f"Task {task_id} marked as completed!")
                else:
                    print(f"Task with ID {task_id} not found.")
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