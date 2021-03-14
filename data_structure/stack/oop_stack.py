"""Stack implementation  using oop style."""

from data_structure.exceptions.stack_exceptions import StackIsEmptyExeption


class Stack(object):
    """Class implements the data structure stack."""

    def __init__(self):
        """List-based stack implementation."""
        self._stack = []
        self._size = 0

    def __str__(self):
        """Return a string representation of the contents of a stack.

        Returns:
            str (string): contents of a stack
        """
        return ','.join(map(str, self._stack))

    def __len__(self):
        """Return size of stack.

        Returns:
            size (int): stack size
        """
        return self._size

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
            size (bool): true if stack is empry, else false
        """
        return self._size == 0

    def push(self, element):
        """Add element in stack.

        Args:
            element:  element for added in stack
        """
        self._stack.append(element)
        self._size += 1

    def pop(self):
        """Extract item from stack.

        Returns:
            item: top item from stack

        Raises:
            StackIsEmptyExeption: if stack is empty
        """
        if self.is_empty:
            raise StackIsEmptyExeption('Stack is empty')
        self._size -= 1
        return self._stack.pop()
