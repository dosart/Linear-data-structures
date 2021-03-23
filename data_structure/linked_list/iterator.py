"""Iterator implementation for linked list."""


class LinkedListIterator(object):
    """Class implements iterator for linked list."""

    def __init__(self, head):
        """Class implements iterator for linked list.

        Args:
            head: first element of LinkedList class
        """
        self._current_ptr = head

    def __iter__(self):
        """Return self.

        Returns:
            self (LinkedListIterator): iterator
        """
        return self

    def __next__(self):
        """Return current data and move iterator forward.

        Returns:
            data: current data

        Raises:
            StopIteration: if passed all elements
        """
        if self._current_ptr is None:
            raise StopIteration
        data = self._current_ptr.data
        self._current_ptr = self._current_ptr.next
        return data
