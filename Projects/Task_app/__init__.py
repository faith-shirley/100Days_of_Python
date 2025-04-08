"""
Todo Application Package.

Purpose:
    This package implements a simple Todo List application following Clean Architecture principles.

Features:
    - Create, list, and update todo items.
    - Separation of core business logic from implementation details.

Components:
    1.TodoEntity:
       - Defines core business entities and rules.

    2.TodoRepository:
       - Responsible for data access and persistence.

    3.TodoUseCase:
       - Implements application-specific business rules.

    4.Main:
       - Entry point and user interface integration.

Notes:
    - This application is developed using a layered approach for clarity and scalability.
"""

from TodoEntity import Todo
from TodoRepository import TodoRepository, InMemoryTodoRepository
from TodoUseCase import TodoUseCase