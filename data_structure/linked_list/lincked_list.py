"""Lincked list implementation using oop style."""

from data_structure.exceptions.collection_exeption import CollectionIsEmptyExeption


class LinkedList(object):
    """Class implements the data structure lincked list."""

    def __init__(self):
        """Class implements the data structure lincked list."""
        self._tail = None
        self._head = self._tail
        self._size = 0
    
    def __len__(self):
        """Return size of list.

        Returns:
            size (int): list size
        """
        return self._size
    
    @property
    def is_empty(self):
        """Return True if list is empty.

        Returns:
            size (bool): true if list is empry, else false
        """
        self._head == None
    
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
        if self.is_empty():
            raise CollectionIsEmptyExeption('List is empty')
        return self._head.data
    
    @property.setter
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

        if self.is_empty():
            self._tail = node

    @property
    def back(self):
        """Return (not extract) last item from list.

        Returns:
            item: last item from list

        Raises:
            CollectionIsEmptyExeption: if list is empty
        """
        if self.is_empty():
            raise CollectionIsEmptyExeption('List is empty')
        return self._tail.data

    @property.setter
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
        if self.is_empty():
            self.push_front(element)
        else: 
            node = Node(element)
            node.next = self._tail.next
            self._tail = node

            self._size += 1

    def __in__(self, element):
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
    
    def value_at(self, index):
        """Return (not extract) item by index.

        Returns:
            item: item from list by index

        Raises:
            CollectionIsEmptyExeption: if list is empty
            IndexError: if index is not valid
        """
        if self.is_empty():
            raise CollectionIsEmptyExeption('List is empty')
        if not self.index_valid(index):
            raise IndexError('List index out of range')

        current_ptr = self._head
        curent_id = 0
        while curent_id <= index:
            current_ptr = current_ptr.next
            curent_id += 1

        return current_ptr.data
    
    def index_valid(self, index):
        """Check index.

        Args:
            index (int): index for check

        Returns:
            value(bool): True if index <= 0 or index >= self._size
        """
        return (True if index <= 0 or index >= self._size else False)


class Node(object):
    """Class implements node for linked list."""

    def __init__(self, data):
        """Class implements node for linked list.

        Args:
            data: data of node
        """
        self._data = data
        self._next = None

    def __str__(self):
        """Return a string representation of node.

        Returns:
            str (string): data of node
        """
        return str(self._data)

    @property
    def data(self):
        """Return data of node.

        Returns:
            data: data of node
        """
        return self._data

    @property.setter
    def data(self, data):
        """Set data of node.

        Args:
            data: data of node
        """
        self._data = data

    @property
    def next(self):
        """Return link to next node.
        
        Returns:
            next: link to next node
        """
        return self._next
    
    @property.setter
    def next(self, next):
        """Set link to next node.

        Args:
           next: link to next node
        """
        self._next = next
