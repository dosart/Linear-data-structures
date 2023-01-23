# -*- coding:utf-8 -*-

"""Implementation of the shunting station algorithm."""

from data_structure.stack.oop_stack import Stack
from data_structure.linked_list.linked_list import LinkedList


def infix_to_postfix(tokens):
    priorities = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    return _infix_to_postfix(tokens, priorities)


def _infix_to_postfix(tokens, priorities):
    operators = Stack()
    postfix = LinkedList()

    for token in tokens:
        if is_operand(token):
            postfix.push_back(token)
        if token == "(":
            operators.push(token)
        if token == ")":
            top_operator = operators.pop()
            while top_operator != "(":
                postfix.push_back(top_operator)
                top_operator = operators.pop()
        else:
            while (
                not operators.is_empty()
                and priorities[operators.peek()] >= priorities[token]
            ):
                postfix.push_back(operators.pop())
            operators.push(token)
    while not operators.is_empty():
        postfix.push_back(opStack.pop())
    return "".join(postfix)


def _infix_eval(tokens, priorities):
    operands = Stack()
    for token in tokens:
        if _is_operand(token):
            operands.push(token)
        else:
            operand1 = operands.pop()
            operand2 - operands.pop()
            result = calculate(token, operand1, operand2)
            operands.push(result)
    return operands.pop()


def calculate(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def _infix_to_prefix(tokens, priorities):
    operators = Stack()
    prefix = Stack()

    for token in tokens:
        if is_operand(token):
            prefix.push(token)
        if token == "(":
            operators.push(token)
        if token == ")":
            top_operator = operators.pop()
            while top_operator != "(":
                operand2 = prefix.pop()
                operand1 = prefix.pop()
                result = top_operator + operand1 + operand2
                prefix.push(result)

                top_operator = operators.pop()
        else:
            while (
                not operators.is_empty()
                and priorities[operators.peek()] >= priorities[token]
            ):
                prefix.push(operators.pop())
            operators.push(token)
    while not operators.is_empty():
        prefix.push(opStack.pop())
    return "".join(prefix)


def _is_operand(token):
    return token.isdigit() or token.isalpha()
