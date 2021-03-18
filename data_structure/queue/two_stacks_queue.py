"""Queue implementation  using two stacks."""

from data_structure.stack.oop_stack import Stack
from data_structure.exceptions.collection_exeption import CollectionIsEmptyExeption


class Queue(object):
    """The implementation using two stacks."""

    def __init__(self):
        """Class implements the data structure queue."""
        self._put_stack = Stack()
        self._extract_stack = Stack()

    def __str__(self):
        """Return a string representation of the contents of a queue.

        Returns:
            str (string): contents of a queue
        """
        return str(self._extract_stack) + str(self._put_stack)

    def __len__(self):
        """Return size of stack.

        Returns:
            size (int): stack size
        """
        return self.size

    @property
    def is_empty(self):
        """Return True if queue is empty.

        Returns:
            size (bool): true if stack is empry, else false
        """
        return self._extract_stack.is_empty and self._put_stack.is_empty

    @property
    def size(self):
        """Return size of stack.

        Returns:
            size (int): queue size
        """
        return self._put_stack.size + self._extract_stack.size

    def enqueue(self, element):
        """Add element in queue.

        Args:
            element:  element for added in queue
        """
        self._put_stack.push(element)

    def dequeue(self):
        """Extract item from queue.

        Returns:
            item: top item from queue

        Raises:
            CollectionIsEmptyExeption: if queue is empty
        """
        if self._extract_stack.is_empty:
            while not self._put_stack.is_empty:
                self._extract_stack.push(self._put_stack.pop())
        if self._extract_stack.is_empty:
            raise CollectionIsEmptyExeption('Queue is empty')
        return self._extract_stack.pop()
