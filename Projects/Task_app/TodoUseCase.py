"""
Use case layer for Todo application.

This module implements the application-specific business rules and workflows.
Use cases orchestrate the flow of data between the user interface and the domain model,
applying business rules as needed. They depend on repository interfaces rather than
concrete implementations, following the Dependency Inversion Principle.
"""

from typing import List
from TodoEntity import Todo
from ITodoRepository import ITodoRepository


class TodoUseCase:
    """
    Implements application-specific business workflows for managing todos.

    This class coordinates operations between the presentation layer and the domain model,
    implementing the various user stories or use cases of the application. It translates
    user intent into domain operations, enforces business rules, and returns appropriate
    results to the caller.

    By depending on the repository interface rather than a concrete implementation,
    this class follows the Dependency Inversion Principle, allowing for flexible
    repository implementations without changing this code.

    Attributes:
        repository (ITodoRepository): The repository used for todo persistence
    """

    def __init__(self, repository: ITodoRepository) -> None:
        """
        Initialize the use case with a repository dependency.

        Args:
            repository: An implementation of ITodoRepository that will be used
                        for all data persistence operations. This follows the
                        dependency injection pattern.

        Raises:
            ValueError: If repository is None
        """
        if repository is None:
            raise ValueError("Repository cannot be None")

        self.repository: ITodoRepository = repository

    def add_task(self, task_id: int, title: str, description: str) -> Todo:
        """
        Add a new task to the todo list.

        This method creates a new Todo entity with the provided information
        and persists it using the repository. It implements validation logic
        for the inputs before creating the entity.

        Args:
            task_id: Unique identifier for the task
            title: Short title of the task
            description: Detailed description of the task

        Returns:
            The newly created and persisted Todo object

        Raises:
            ValueError: If id is negative, or if title is empty
        """
        # Input validation
        if task_id < 0:
            raise ValueError("Task ID must be non-negative")
        if not title or title.isspace():
            raise ValueError("Task title cannot be empty")

        # Create a new Todo entity
        todo = Todo(task_id, title, description)

        # Store it using the repository
        self.repository.save(todo)

        return todo

    def list_all_tasks(self) -> List[Todo]:
        """
        Retrieve all tasks in the todo list.

        This method fetches all tasks from the repository and returns them without
        any filtering or sorting.

        Returns:
            A list of all Todo objects in the system.
            Returns an empty list if no tasks exist.
        """
        return self.repository.get_all()

    def mark_task_as_completed(self, task_id: int) -> bool:
        """
        Mark a specific task as completed.

        This method implements the workflow for completing a task:
        1. Find the task by ID
        2. If found, update its completion status
        3. Save the updated entity

        Args:
            task_id: The ID of the task to mark as completed

        Returns:
            True if the task was found and marked as completed,
            False if no task with the given ID exists

        Raises:
            ValueError: If task_id is negative
        """
        if task_id < 0:
            raise ValueError("Task ID must be non-negative")

        # Retrieve the Todo entity
        todo = self.repository.get_by_id(task_id)

        if todo:
            # Apply the business rule to mark it as completed
            todo.mark_as_completed()

            # Save the updated entity
            self.repository.save(todo)
            return True

        return False