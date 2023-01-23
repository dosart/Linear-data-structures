"""Node implementation for linked list."""


class Node(object):
    """Class implements node for linked list."""

    def __init__(self, init_data):
        """Class implements node for linked list.

        Args:
            init_data: data of node
        """
        self.data = init_data
        self.next = None

    def __str__(self):
        """Return a string representation of node.

        Returns:
            str (string): data of node
        """
        return str(self.data)
