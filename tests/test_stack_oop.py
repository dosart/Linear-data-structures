"""Tests of oop stack."""

import pytest

from data_structure.stack.oop_stack import Stack
from data_structure.exceptions.collection_exeption import CollectionIsEmptyExeption
from data_structure.exceptions.error_messages import stack_is_empty


def test_make_stack():
    stack = Stack()

    assert stack.is_empty is True
    assert stack.size == 0
    assert len(stack) == 0


def test_push_positive():
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.size == 3
    assert stack.is_empty is False


def test_pop_positive():
    stack = Stack()

    stack.push(15)
    stack.push(25)
    stack.push(35)
    stack.push(45)

    assert stack.size == 4
    assert stack.is_empty is False
    assert stack.pop() == 45
    assert stack.size == 3
    assert stack.is_empty is False


def test_push_and_pop():
    stack = Stack()

    stack.push(25)
    stack.push(35)
    stack.push(45)
    stack.push(55)

    assert stack.size == 4
    assert stack.is_empty is False
    assert stack.pop() == 55
    assert stack.size == 3
    assert stack.is_empty is False

    assert stack.pop() == 45
    assert stack.pop() == 35
    assert stack.pop() == 25


def test_push_and_pop2():
    stack = Stack()

    for i in range(10):
        stack.push(i)

    assert stack.pop() == 9
    assert stack.pop() == 8

    stack.push(10)
    stack.push(11)

    assert stack.pop() == 11
    assert stack.pop() == 10


def test_pop_from_empty_stack():
    stack = Stack()

    with pytest.raises(CollectionIsEmptyExeption) as exception_info:
        value = stack.pop()

    assert str(exception_info.value) == stack_is_empty()


def test_to_empty_string():
    stack = Stack()

    assert "" == str(stack)


def test_to_string():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert "1,2,3" == str(stack)


def test_len_function():
    stack = Stack()

    stack.push(11)
    stack.push(12)
    stack.push(13)

    assert len(stack) == 3


def test_peek_function1():
    stack = Stack()

    stack.push(11)
    stack.push(12)
    stack.push(13)

    assert stack.peek() == 13
    assert stack.peek() == 13
    assert stack.peek() == 13
    assert len(stack) == 3


def test_peek_function2():
    stack = Stack()

    stack.push(11)
    stack.push(12)
    stack.push(13)

    assert stack.peek() == 13
    assert stack.pop() == 13
    assert len(stack) == 2

    assert stack.peek() == 12
    assert stack.pop() == 12
    assert len(stack) == 1

    assert stack.peek() == 11
    assert stack.pop() == 11
    assert len(stack) == 0


def test_peek_function3():
    stack = Stack()

    stack.push(11)

    assert stack.peek() == 11
    assert stack.pop() == 11
    assert len(stack) == 0

    stack.push(12)
    stack.push(13)
    assert stack.peek() == 13
    assert stack.pop() == 13
    assert len(stack) == 1


def test_stack_iterator():
    stack = Stack()
    stack.push(10)
    stack.push(30)
    stack.push(20)

    for elem in stack:
        pass


def test_stack_pop_while():
    values = [0, 1, 2, 3, 4, 5]
    stack = Stack()

    for value in values:
        stack.push(value)

    for value in stack.pop_while(lambda x: x != 2):
        assert value > 1
