"""Queue implementation using oop style."""

from data_structure.base_collection import BaseCollection, Position
from data_structure.exceptions.collection_exeption import CollectionIsEmptyExeption


class Queue(object):
    """List-based queue implementation."""

    def __init__(self):
        """Class implements the data structure queue."""
        self._queue = BaseCollection()

    def __str__(self):
        """Return a string representation of the contents of a queue.

        Returns:
            str (string): contents of a queue
        """
        return str(self._queue)

    def __len__(self):
        """Return size of stack.

        Returns:
            size (int): stack size
        """
        return self._queue.size

    @property
    def size(self):
        """Return size of queue.

        Returns:
            size (int): queue size
        """
        return self._queue.size

    @property
    def is_empty(self):
        """Return True if queue is empty.

        Returns:
            size (bool): true if stack is empry, else false
        """
        return self._queue.is_empty

    def enqueue(self, element):
        """Add element in queue.

        Args:
            element:  element for added in queue
        """
        self._queue.insert(element, Position.first)

    def dequeue(self):
        """Extract item from queue.

        Returns:
            item: top item from queue

        Raises:
            CollectionIsEmptyExeption: if queue is empty
        """
        if self._queue.is_empty:
            raise CollectionIsEmptyExeption('Queue is empty')
        return self._queue.extract()
