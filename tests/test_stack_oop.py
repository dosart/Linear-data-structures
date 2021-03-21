"""Tests of oop stack."""

import pytest

from data_structure.stack.oop_stack import Stack
from data_structure.exceptions.collection_exeption import CollectionIsEmptyExeption
from data_structure.exceptions.error_messages import stack_is_empty


def test_make_stack():
    stack = Stack()

    assert stack.is_empty == True
    assert stack.size == 0
    assert len(stack) == 0


def test_push_positive():
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.size == 3
    assert stack.is_empty == False


def test_pop_positive():
    stack = Stack()

    stack.push(15)
    stack.push(25)
    stack.push(35)
    stack.push(45)

    assert stack.size == 4
    assert stack.is_empty == False
    assert stack.pop() == 45
    assert stack.size == 3
    assert stack.is_empty == False


def test_push_and_pop():
    stack = Stack()

    stack.push(25)
    stack.push(35)
    stack.push(45)
    stack.push(55)

    assert stack.size == 4
    assert stack.is_empty == False
    assert stack.pop() == 55
    assert stack.size == 3
    assert stack.is_empty == False

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

    assert '' == str(stack)


def test_to_string():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert '1,2,3' == str(stack)


def test_len_function():
    stack = Stack()

    stack.push(11)
    stack.push(12)
    stack.push(13)

    assert len(stack) == 3
