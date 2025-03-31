"""
Interface layer for Todo application.
This module contains the repository interfaces and implementations.
"""

class TodoRepository:
    """
    Abstract base class defining the interface for todo storage.

    Any concrete repository implementation must provide these methods.
    This follows the Repository pattern and Dependency Inversion principle.
    """

    def save(self, todo):
        """
        Save a todo item to the repository.

        Args:
            todo: The Todo object to save

        Raises:
            NotImplementedError: This is an abstract method
        """
        raise NotImplementedError("Subclasses must implement save()")

    def get_all(self):
        """
        Retrieve all todo items from the repository.

        Returns:
            A list of Todo objects

        Raises:
            NotImplementedError: This is an abstract method
        """
        raise NotImplementedError("Subclasses must implement get_all()")

    def get_by_id(self, todo_id):
        """
        Retrieve a specific todo item by its ID.

        Args:
            todo_id: The ID of the todo item to retrieve

        Returns:
            The Todo object if found, None otherwise

        Raises:
            NotImplementedError: This is an abstract method
        """
        raise NotImplementedError("Subclasses must implement get_by_id()")

class InMemoryTodoRepository(TodoRepository):
    """
    Implementation of TodoRepository that stores todos in memory.

    This provides a simple storage solution using a Python dictionary.
    In a real application, this might be replaced with a database-backed implementation.
    """

    def __init__(self):
        """Initialize an empty repository."""
        self.todos = {}  # Dictionary to store todos with ID as key

    def save(self, todo):
        """
        Save a todo item to the in-memory store.

        Args:
            todo: The Todo object to save
        """
        self.todos[todo.id] = todo

    def get_all(self):
        """
        Retrieve all todo items from the in-memory store.

        Returns:
            A list of all Todo objects
        """
        return list(self.todos.values())

    def get_by_id(self, todo_id):
        """
        Retrieve a specific todo item by its ID.

        Args:
            todo_id: The ID of the todo item to retrieve

        Returns:
            The Todo object if found, None otherwise
        """
        return self.todos.get(todo_id)