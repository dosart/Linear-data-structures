"""Iterator implementation for linked list."""


class LinkedListIterator(object):
    """Class implements iterator for linked list."""

    def __init__(self, head):
         """Class implements iterator for linked list.
         
         Args:
            linked_list(LinkedList): linked list
         """
         self._current_ptr = head
    
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
            data = self._current_ptr.data
            self._current_ptr = self._current_ptr.next
            return data
        else:
            raise StopIteration
