"""Stack implementation  using imperative style (only functions)."""


from exceptions.stack_exceptions import StackIsEmptyExeption


def make_stack():
    """Return data structure stack.

    Returns:
        stack data structure
    """
    return {_collection_key(): [], _size_key(): 0}


def push(stack, element):
    """Add element in stack.

    Args:
        stack: stack data structure (created by function make_stack())
        element:  element for added in stack
    """
    collection = _get_collection(stack)
    collection.append(element)
    _add_size(stack, 1)


def pop(stack):
    """Extract item from stack.

    Args:
        stack: stack data structure (created by function make_stack())

    Returns:
        item: top item from stack

    Raises:
        StackIsEmptyExeption: if stack is empty
    """
    if is_empty(stack):
        raise StackIsEmptyExeption('Stack is Empty')
    _add_size(stack, -1)
    return stack[_collection_key()].pop()


def is_empty(stack):
    """Return True if stack is empty.

    Args:
        stack: stack data structure (created by function make_stack())

    Returns:
        size (bool): true if stack is empry, else false
    """
    size = _get_size(stack)
    return (size == 0)


def size(stack):
    """Return size of stack.

    Args:
        stack: stack data structure (created by function make_stack())

    Returns:
        size (int): stack size
    """
    return _get_size(stack)


def _get_collection(stack):
    return stack[_collection_key()]


def _get_size(stack):
    return stack[_size_key()]


def _add_size(stack, added_value):
    stack[_size_key()] += added_value


def _size_key():
    return 'size'


def _collection_key():
    return 'collection'
