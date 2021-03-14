"""Tests of oop stack."""

import pytest

from data_structure.stack.oop_stack import Stack
from data_structure.exceptions.stack_exceptions import StackIsEmptyExeption


def test_make_stack():
    stack = Stack()

    assert stack.is_empty == True
    assert stack.size == 0


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

    
    stack.push(65)
    stack.push(75)

    assert stack.size == 5
    assert stack.is_empty == False
    assert stack.pop() == 75
    assert stack.size == 4
    assert stack.is_empty == False


def test_pop_from_empty_stack():
    stack = Stack()

    with pytest.raises(StackIsEmptyExeption) as exception_info:
        value = stack.pop()
    
    assert str(exception_info.value) == 'Stack is empty'


def test_to_empty_string():
    stack = Stack()

    assert '' == stack.__str__()


def test_to_string():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert '1,2,3' == stack.__str__()


def test_len_is_zero():
    stack = Stack()

    assert len(stack) == 0


def test_len_function():
    stack = Stack()

    stack.push(11)
    stack.push(12)
    stack.push(13)

    assert len(stack) == 3
