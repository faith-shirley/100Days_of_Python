"""
Use case layer for Todo application.
This module contains the application-specific business rules.
"""

from TodoEntity import Todo

class TodoUseCase:
    """
    Implements the application-specific business rules for managing todos.

    This class orchestrates the flow of data to and from the entities,
    and directs the entities to use their core business rules to achieve the use case.
    """

    def __init__(self, repository):
        """
        Initialize the use case with a repository.

        Args:
            repository: An implementation of TodoRepository
        """
        self.repository = repository

    def add_task(self, id, title, description):
        """
        Add a new task to the todo list.

        Args:
            id: Unique identifier for the task
            title: Short title of the task
            description: Detailed description of the task

        Returns:
            The newly created Todo object
        """
        # Create a new Todo entity
        todo = Todo(id, title, description)

        # Store it using the repository
        self.repository.save(todo)

        return todo

    def list_all_tasks(self):
        """
        List all tasks in the todo list.

        Returns:
            A list of all Todo objects
        """
        return self.repository.get_all()

    def mark_task_as_completed(self, task_id):
        """
        Mark a specific task as completed.

        Args:
            task_id: The ID of the task to mark as completed

        Returns:
            True if the task was found and marked as completed, False otherwise
        """
        # Retrieve the Todo entity
        todo = self.repository.get_by_id(task_id)

        if todo:
            # Apply the business rule to mark it as completed
            todo.mark_as_completed()

            # Save the updated entity
            self.repository.save(todo)
            return True

        return False