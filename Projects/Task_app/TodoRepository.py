"""
Repository layer for Todo application.

This module contains concrete implementations of the ITodoRepository interface.
It provides the data access layer that interacts with the chosen storage technology,
while adhering to the contract defined by the repository interface.
"""
from typing import Dict, List, Optional
from TodoEntity import Todo
from ITodoRepository import ITodoRepository


class InMemoryTodoRepository(ITodoRepository):
    """
    In-memory implementation of the todo repository interface.

    This repository stores todos in a Python dictionary for the application's lifetime.
    It's suitable for testing, prototyping, or applications that don't require persistent storage.

    Note that all data is lost when the application terminates.

    Attributes:
        todos (Dict[int, Todo]): Dictionary mapping todo IDs to Todo objects
    """

    def __init__(self) -> None:
        """
        Initialize an empty repository with no todos.

        Creates an empty dictionary that will store todos indexed by their IDs,
        allowing for fast lookup by ID.
        """
        self.todos: Dict[int, Todo] = {}

    def save(self, todo: Todo) -> None:
        """
        Save a todo item in the in-memory dictionary.

        This method handles both creating new todos and updating existing ones,
        determining which action to take based on whether the todo already exists
        in the repository.

        Args:
            todo: The Todo object to save

        Raises:
            ValueError: If todo is None or missing an ID
        """
        if todo is None:
            raise ValueError("Cannot save None as a todo")
        if todo.id is None:
            raise ValueError("Todo must have an ID to be saved")

        self.todos[todo.id] = todo

    def get_all(self) -> List[Todo]:
        """
        Retrieve all stored todo items.

        Returns:
            A list containing all Todo objects in the repository.
            Returns an empty list if no todos exist.
        """
        return list(self.todos.values())

    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Retrieve a specific todo item by its ID.

        Uses dictionary lookup to efficiently find a todo by its ID.

        Args:
            todo_id: The ID of the todo item to retrieve

        Returns:
            The matching Todo object if found, None if no todo with the given ID exists

        Raises:
            ValueError: If todo_id is None or not an integer (e.g., negative)
        """
        if todo_id is None:
            raise ValueError("Todo ID cannot be None")

        return self.todos.get(todo_id) # Returns None if ID doesn't exist