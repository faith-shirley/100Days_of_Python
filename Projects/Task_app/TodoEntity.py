"""
Entity layer for Todo application.

This module defines the core domain entities that represent the business objects
in our todo application. These entities encapsulate the critical business rules
and data that are essential to the application, independent of any UI or data storage concerns.
"""
from typing import Optional


class Todo:
    """
    Represents a task in the to-do list with its core properties and behaviors.

    This entity encapsulates the fundamental concept of a "task" in our domain,
    maintaining its state (completion status) and identity. The business rules
    related to task management (like marking complete) are contained within this class.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Short descriptive name of the task
        description (str): Detailed explanation of what the task involves
        completed (bool): Whether the task has been completed, defaults to False
    """

    def __init__(self, task_id: int, title: str, description: str) -> None:
        """
        Initialize a new Todo item with required fields and default completion status.

        Args:
            task_id: Unique identifier for the task, must be unique within the system
            title: Short descriptive name of the task (1-50 characters recommended)
            description: Detailed explanation of what the task involves
        """
        self.id: int = task_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False #All new tasks start as incomplete

    def mark_as_completed(self) -> None:
        """
        Mark the task as completed.

        This method implements the business logic for changing a task's state to complete.
        Once marked as completed, the task's status can be used for reporting or filtering.
        """
        self.completed = True

    def __str__(self) -> str:
        """
        Create a human-readable string representation of the task.

        Returns a formatted string containing:
            - a checkbox indicating completion status
            - the task ID
            - the task title
            - the task description

        Example:
            "[✓] 1: Complete project - Finish the Todo application"
        """
        status = "\u2713" if self.completed else "\u2610" # ✓ or ☐
        return f"[{status}] {self.id}: {self.title} - {self.description}"