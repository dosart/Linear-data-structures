"""Iterator implementation for linked list."""


class LinkedListIterator(object):
    """Class implements iterator for linked list."""

    def __init__(self, linked_list):
         """Class implements iterator for linked list.
         
         Args:
            linked_list(LinkedList): linked list
         """
         self._list = linked_list
         self._current_ptr = linked_list._head
    
    def __iter__(self):
        """Return self.
        
        Args:
            self(LinkedListIterator): self
        """
        return self
    
    def __next__(self):
        """Return current data and move iterator forward.
        
        Returns:
            data: current data

        Raises:
            StopIteration: if passed all elements
        """
        if self._current_ptr is not None:
            data = self._current_ptr._head
            self._current_ptr = self._current_ptr.next
            return data
        else:
            raise StopIteration
