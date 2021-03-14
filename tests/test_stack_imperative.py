"""Tests of imperative stack."""

import pytest

from data_structure.stack.imperative_stack import make_stack, push, pop, is_empty, size
from data_structure.exceptions.stack_exceptions import StackIsEmptyExeption


def test_make_stack():
    stack = make_stack()

    assert size(stack) == 0
    assert is_empty(stack) == True


def test_push_positive():
    stack = make_stack()
    push(stack, 1)
    push(stack, 2)
    push(stack, 3)

    assert size(stack) == 3
    assert is_empty(stack) == False


def test_pop_positive():
    stack = make_stack()
    push(stack, 10)
    push(stack, 20)

    assert pop(stack) == 20
    assert is_empty(stack) == False


def test_push_and_pop1():
    stack = make_stack()
    push(stack, 1)
    push(stack, 2)

    assert is_empty(stack) == False
    assert size(stack) == 2

    assert pop(stack) == 2
    assert is_empty(stack) == False
    assert size(stack) == 1


def test_push_and_pop2():
    stack = make_stack()
    push(stack, 10)
    push(stack, 20)

    assert is_empty(stack) == False
    assert size(stack) == 2
    assert pop(stack) == 20

    push(stack, 30)
    push(stack, 40)
    push(stack, 50)

    assert is_empty(stack) == False
    assert size(stack) == 4
    assert pop(stack) == 50
    assert size(stack) == 3



def test_pop_from_empty_stack():
    stack = make_stack()

    with pytest.raises(StackIsEmptyExeption) as exception_info:
        value = pop(stack)
    
    assert str(exception_info.value) == 'Stack is Empty'
