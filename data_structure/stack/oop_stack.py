"""Stack implementation  using oop style."""

from data_structure.base_collection import BaseCollection, Position
from data_structure.exceptions.collection_exeption import (
    CollectionIsEmptyExeption,
)
from data_structure.exceptions.error_messages import stack_is_empty


class Stack(object):
    """Class implements the data structure stack."""

    def __init__(self):
        """List-based stack implementation."""
        self._stack = BaseCollection()

    def __str__(self):
        """Return a string representation of the contents of a stack.

        Returns:
            str (string): contents of a stack
        """
        return str(self._stack)

    def __len__(self):
        """Return size of stack.

        Returns:
            size (int): stack size
        """
        return self._stack.size

    @property
    def size(self):
        """Return size of stack.

        Returns:
            size (int): stack size
        """
        return self._stack.size

    @property
    def is_empty(self):
        """Return True if stack is empty.

        Returns:
            size (bool): true if stack is empry, else false
        """
        return self._stack.size == 0

    def push(self, element):
        """Add element in stack.

        Args:
            element:  element for added in stack
        """
        self._stack.insert(element, Position.last)

    def pop(self):
        """Extract item from stack.

        Returns:
            item: top item from stack

        Raises:
            CollectionIsEmptyExeption: if stack is empty
        """
        if self.is_empty:
            raise CollectionIsEmptyExeption(stack_is_empty())
        return self._stack.extract()

    def peek(self):
        """Return the element at the top of the stack.

        Returns:
            value: element at the top of the stack

        Raises:
            CollectionIsEmptyExeption: if stack is empty
        """
        if self.is_empty:
            raise CollectionIsEmptyExeption(stack_is_empty())
        return self._stack.peek()
