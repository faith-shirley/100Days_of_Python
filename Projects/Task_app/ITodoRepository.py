"""
Repository interface layer for Todo application.

This module defines the abstract contract that any todo storage implementation must follow.
Following the Dependency Inversion Principle, this interface allows higher-level modules
to depend on abstractions rather than concrete implementations, enabling flexibility
in storage solutions without affecting business logic.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from TodoEntity import Todo


class ITodoRepository(ABC):
    """
    Abstract interface for todo storage operations.

    This interface defines the contract that any todo storage implementation must adhere to.
    It ensures that regardless of the actual storage mechanism (in-memory, database, file, etc.),
    the core application logic can interact with it in a consistent way.

    By defining this interface in the domain layer, we enforce the Dependency Inversion
    Principle - higher-level modules depend on this abstraction rather than specific implementations.
    """

    @abstractmethod
    def save(self, todo: Todo) -> None:
        """
        Persist a todo item to the storage system.

        This method handles both creating new todos and updating existing ones,
        determining which action to take based on whether the todo already exists
        in the repository.

        Args:
            todo: The Todo object to save

        Raises:
            ValueError: If the todo object is invalid (implementation-specific)
            StorageError: If the storage operation fails (implementation-specific)
        """
        pass

    @abstractmethod
    def get_all(self) -> List[Todo]:
        """
        Retrieve all stored todo items.

        This method returns all todos currently in the system without any filtering.
        The returned list may be empty if no todos exist.

        Returns:
            A list of all Todo objects in the system, ordered by ID (implementation-specific)

        Raises:
            StorageError: If the retrieval operation fails (implementation-specific)
        """
        pass

    @abstractmethod
    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Retrieve a specific todo item by its unique identifier.

        This method looks up a single todo using its ID. If no todo with the
        specified ID exists, it returns None rather than raising an exception.

        Args:
            todo_id: The unique identifier of the todo item to retrieve

        Returns:
            The matching Todo object if found, None otherwise

        Raises:
            ValueError: If todo_id is invalid (e.g., negative)
            StorageError: If the retrieval operation fails (implementation-specific)
        """
        pass