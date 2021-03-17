"""Stack implementation  using imperative style (only functions)."""

from data_structure.exceptions.collection_exeption import CollectionIsEmptyExeption


def make_stack():
    """Return data structure stack.

    Returns:
        stack data structure
    """
    return _make_collection()


def push(stack, element):
    """Add element in stack.

    Args:
        stack: stack data structure (created by function make_stack())
        element:  element for added in stack
    """
    _insert(stack, element)


def pop(stack):
    """Extract item from stack.

    Args:
        stack: stack data structure (created by function make_stack())

    Returns:
        item: top item from stack

    Raises:
        CollectionIsEmptyExeption: if stack is empty
    """
    if is_empty(stack):
        raise CollectionIsEmptyExeption('Stack is Empty')
    return _extract(stack)


def is_empty(stack):
    """Return True if stack is empty.

    Args:
        stack: stack data structure (created by function make_stack())

    Returns:
        size (bool): true if stack is empry, else false
    """
    return _size(stack) == 0


def size(stack):
    """Return size of stack.

    Args:
        stack: stack data structure (created by function make_stack())

    Returns:
        size (int): stack size
    """
    return _size(stack)


def _make_collection():
    return []


def _insert(collection, element):
    collection.append(element)


def _extract(collection):
    return collection.pop()


def _size(collection):
    return len(collection)
