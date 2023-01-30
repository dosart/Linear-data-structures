# -*- coding:utf-8 -*-

"""Implementation of the shunting station algorithm."""

import string
from operator import add, mul, sub, truediv

from calculations.either import make_left, make_right
from data_structure.linked_list.linked_list import LinkedList
from data_structure.stack.oop_stack import Stack


def infix_to_postfix(tokens):
    """Translate an exprassion from an infix form to a postfix form.

    Args:
        tokens: iterable string object in infix form

    Returns:
        string in a postfix form
    """
    without_whitespace = tokens.translate(
        {ord(char): None for char in string.whitespace},
    )
    priorities = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    return _infix_to_postfix(without_whitespace, priorities)


def postfix_eval(tokens):
    """Eval an exprassion in a postfix form.

    Args:
        tokens: the iterable string object in infix form

    Returns:
        result(monad's either): the result calculating the postfix exprassion
    """
    operands = Stack()
    for token in tokens:
        if _is_operand(token):
            operands.push(token)
        else:
            if operands.is_empty:
                return make_left("The left operand is incorrect")
            operand1 = operands.pop()

            if operands.is_empty:
                return make_left("The right operand is incorrect")
            operand2 = operands.pop()

            result = _try_calculate(token, operand1, operand2)
            if result.is_left:
                return result
            operands.push(result.get_right())

    return make_right(operands.pop())


def _try_calculate(op, op1, op2):
    if not _is_int(op1):
        return make_left("The left operand is incorrect")
    if not _is_int(op2):
        return make_left("The right operand is incorrect")
    if not _is_operator(op):
        return make_left("The operator is incorrect")
    return make_right(_calculate(op, int(op1), int(op2)))


def _is_int(element):
    if element is None:
        return False
    try:
        int(element)
        return True
    except ValueError:
        return False


def _is_operator(op):
    return op in _make_operators()


def _calculate(op, op1, op2):
    operators = _make_operators()
    operator = operators[op]
    return operator(op1, op2)


def _make_operators():
    return {"*": mul, "+": add, "-": sub, "/": truediv}


def _infix_to_postfix(tokens, priorities):
    operators = Stack()
    postfix = LinkedList()

    for token in tokens:
        if _is_operand(token):
            postfix.push_back(token)
        elif token == "(":
            operators.push(token)
        elif token == ")":
            for operator in operators.pop_while(lambda opr: opr != "("):
                postfix.push_back(operator)
            operators.pop()
        else:
            top_higher_priority = _make_comparator(priorities, token)
            for operator in operators.pop_while(top_higher_priority):
                postfix.push_back(operator)
            operators.push(token)
    for operator in operators.pop_while(lambda _: True):
        postfix.push_back(operator)
    return "".join(postfix)


def _make_comparator(priorities, token):
    def predicat(operator):
        return priorities[operator] >= priorities[token]

    return predicat


def _is_operand(token):
    return token.isdigit() or token.isalpha()
