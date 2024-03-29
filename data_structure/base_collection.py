"""Collection for stack and queue."""

from enum import Enum


class Position(Enum):
    """Position to extract and insert element in collection."""

    first = 0
    last = 1


class BaseCollection(object):
    """Class implements the data structure array."""

    def __init__(self):
        """Array implementation."""
        self._collection = []
        self._size = 0

    def __str__(self):
        """Return a string representation of the contents.

        Returns:
            str (string): contents of a collection
        """
        return ",".join(map(str, self._collection))

    def __len__(self):
        """Return size of collection.

        Returns:
            size (int): stack size
        """
        return self._size

    def __iter__(self):
        """Return iterator.

        Returns:
            iterator (BaseCollection): iterator
        """
        return iter(self._collection)

    @property
    def size(self):
        """Return size of stack.

        Returns:
            size (int): stack size
        """
        return self._size

    @property
    def is_empty(self):
        """Return True if stack is empty.

        Returns:
            size (bool): true if stack is empty, else false
        """
        return self._size == 0

    def insert(self, element, position=Position.last):
        """Insert element in collection.

        By default, inserts at the end

        Args:
            element: element for added in collection
            position (Position): last append to the end, first append to begin
        """
        if position == Position.last:
            self._collection.append(element)
        else:
            self._collection.insert(0, element)
        self._size += 1

    def extract(self, position=Position.last):
        """Extract and remove element in collection.

        Doesn't check if the collection is empty

        Args:
            position (Position): last append to the end, first append to begin

        Returns:
            element: element of collection
        """
        if position == Position.last:
            self._size -= 1
            return self._collection.pop()
        self._size -= 1
        return self._collection.pop(0)

    def peek(self, position=Position.last):
        """Return the element at the top of the stack.

        Args:
            position (Position): last append to the end, first append to begin

        Returns:
            value: element at the top of the stack
        """
        if position == Position.last:
            return self._collection[self._size - 1]
        return self._collection[0]
