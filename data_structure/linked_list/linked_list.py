"""Lincked list implementation using oop style."""

from data_structure.exceptions.collection_exeption import (
    CollectionIsEmptyExeption,
)
from data_structure.exceptions.error_messages import (
    index_out_of_range,
    list_is_empty,
)
from data_structure.linked_list.iterator import LinkedListIterator
from data_structure.linked_list.node import Node


class LinkedList(object):
    """Class implements the data structure lincked list."""

    def __init__(self):
        """Class implements the data structure lincked list."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return size of list.

        Returns:
            size (int): list size
        """
        return self._size

    def __iter__(self):
        """Return iterator of list.

        Returns:
            iterator (LinkedListIterator): iterator of list
        """
        return LinkedListIterator(self._head)

    @property
    def is_empty(self):
        """Return True if list is empty.

        Returns:
            size (bool): true if list is empty, else false
        """
        return self._size == 0

    @property
    def size(self):
        """Return size of list.

        Returns:
            size (int): list size
        """
        return self._size

    @property
    def front(self):
        """Return (not extract) first item from list.

        Returns:
            item: first item from list

        Raises:
            CollectionIsEmptyExeption: if list is empty
        """
        if self.is_empty:
            raise CollectionIsEmptyExeption(list_is_empty())
        return self._head.data

    @front.setter
    def front(self, element):
        """Add element in list front.

        Args:
            element:  element for added in list
        """
        self.push_front(element)

    def push_front(self, element):
        """Add element in list front.

        Args:
            element:  element for added in list
        """
        node = Node(element)
        node.next = self._head
        self._head = node

        self._size += 1

    @property
    def back(self):
        """Return (not extract) last item from list.

        Returns:
            item: last item from list
        """
        return self.value_at(self._size - 1)

    @back.setter
    def back(self, element):
        """Add element in list back.

        Args:
            element:  element for added in list
        """
        self.push_back(element)

    def push_back(self, element):
        """Add element in list front.

        Args:
            element:  element for added in list
        """
        if self.is_empty:
            self.push_front(element)
        else:
            node = Node(element)

            current = self._head
            while current.next:
                current = current.next
            current.next = node

            self._size += 1

    def __contains__(self, element):
        """Check contain element in list.

        Args:
            element: element of list

        Returns:
            true if element contains in list
        """
        return self.contains(element)

    def contains(self, element):
        """Check contain element in list.

        Args:
            element: element of list

        Returns:
            true if element contains in list
        """
        current_ptr = self._head
        while current_ptr:
            if current_ptr.data == element:
                return True
            current_ptr = current_ptr.next
        return False

    def erase(self, index):
        """Remove element by index from list.

        Args:
            index (int): index of element for delete

        Raises:
            CollectionIsEmptyExeption: if list is empty
        """
        if self.is_empty:
            raise CollectionIsEmptyExeption(self._error_message)
        if index == 0:
            self.pop_front()
            return
        if index == self._size - 1:
            self.pop_back()
            return
        previous = self._find_by(index - 1)
        deleted = previous.next
        previous.next = deleted.next
        deleted.next = None

        self._size -= 1

    def pop_front(self):
        """Return (and extract) first item from list.

        Returns:
            first_element_data: first item from list

        Raises:
            CollectionIsEmptyExeption: if list is empty
        """
        if self.is_empty:
            raise CollectionIsEmptyExeption(list_is_empty())

        return_value = self._head.data

        self._head = self._head.next
        self._size -= 1

        return return_value

    def pop_back(self):
        """Return (and extract) last item from list.

        Returns:
            last_item: last item from list

        Raises:
            CollectionIsEmptyExeption: if list is empty
        """
        if self.is_empty:
            raise CollectionIsEmptyExeption(list_is_empty())

        penultimate = self._find_by(self._size - 2)
        last = penultimate.next
        penultimate.next = None
        self._size -= 1

        return last.data

    def remove_value(self, value):
        """Remove element by value from list.

        Args:
            value (int): value of element for delete

        Returns:
            result (bool): if value removed return True, else False
        """
        current = self._head
        previously = Node
        founded = False

        while current is not None and founded is not True:
            if current.data == value:
                founded = True
            else:
                previously = current
                current = current.next

        if current is None:
            return False

        if current is self._head:
            node = self._head
            self._head = self._head.next
            node.next = None
        else:
            previously.next = current.next
            current.next = None

        self._size -= 1
        return True

    def value_at(self, index):
        """Return (not extract) item by index.

        Returns:
            item: item from list by index

        Args:
            index (int): index return item

        Raises:
            CollectionIsEmptyExeption: if list is empty
            IndexError: if index is not valid
        """
        if self.is_empty:
            raise CollectionIsEmptyExeption(list_is_empty())
        if not self.index_valid(index):
            raise IndexError(index_out_of_range())

        finded = self._find_by(index)
        return finded.data

    def insert(self, index, value):
        """Insert item by index.

        Args:
            index (int): index for insert
            value : value for insert

        Raises:
            CollectionIsEmptyExeption: if list is empty
            IndexError: if index is not valid
        """
        if self.is_empty:
            raise CollectionIsEmptyExeption(list_is_empty())
        if not self.index_valid(index):
            raise IndexError(index_out_of_range())
        if index == 0:
            self.push_front(value)
            return
        else:
            node = Node(value)
            previously = self._find_by(index - 1)
            node.next = previously.next
            previously.next = node

            self._size += 1

    def index_valid(self, index):
        """Check index.

        Args:
            index (int): index for check

        Returns:
            value(bool): True if index >= 0 or index <= self._size
        """
        return True if index >= 0 or index <= self._size

    def _find_by(self, index):
        current_id = 0
        current_ptr = self._head

        while current_id < index:
            current_id += 1
            current_ptr = current_ptr.next

        return current_ptr
