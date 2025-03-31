"""
Entity layer for Todo application.
This module contains the core business entities.
"""


class Todo:
    """
    Represents a task in the to-do list.

    This class contains the core business logic for a task,
    independent of any external systems or use cases.
    """

    def __init__(self, id, title, description):
        """
        Initialize a new Todo item.

        Args:
            id: Unique identifier for the task
            title: Short title of the task
            description: Detailed description of the task
        """
        self.id = id
        self.title = title
        self.description = description
        self.completed = False  # Tasks always start as not completed

    def mark_as_completed(self):
        """Mark this task as completed."""
        self.completed = True

    def __str__(self):
        """
        Return a string representation of the task.

        Returns:
            A formatted string showing the task's status, ID, title, and description.
        """
        status = "\u2713" if self.completed else "\u2610"
        return f"[{status}] {self.id}: {self.title} - {self.description}"