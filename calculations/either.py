# -*- coding:utf-8 -*-

"""Monad Either's implementation."""


class Either(object):
    """Monad Either's implementation."""

    def __init__(self, value, is_left):
        """Construct a new either.

        Args:
            value: error message or correct value
            is_left: True if the value contains an error message
        """
        self.value = value
        self.is_left_value = is_left

    @property
    def is_left(self):
        """Return True if the value contains an error message.

        Returns:
            is_left_value: the contents of the variable
        """
        return self.is_left_value

    def get_left(self):
        """Return an error message.

        Raises:
            RuntimeError: if the is_left function returns False.

        Returns:
            value: an error message
        """
        if not self.is_left:
            raise RuntimeError("Value is not defined")
        return self.value

    @property
    def is_right(self):
        """Return True if the value contains value.

        Returns:
            is_left_value: the contents of the variable
        """
        return not self.is_left

    def get_right(self):
        """Return an error message.

        Raises:
            RuntimeError: if the is_right function returns False.

        Returns:
            value: value
        """
        if not self.is_right:
            raise RuntimeError("Value is not defined")
        return self.value


def make_left(value):
    """Return either with error message.

    Args:
        value: error message

    Returns:
        either: either with error message
    """
    return Either(value=value, is_left=True)


def make_right(value):
    """Return either with saved value.

    Args:
        value: value to save

    Returns:
        either: either with value
    """
    return Either(value=value, is_left=False)


def make_error_message(message):
    """Return error message.

    Args:
        message: error message

    Returns:
        str: error message
    """
    return "Error: {0}".format(message.lower())
