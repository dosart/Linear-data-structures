"""Tests of the shunting station algorithm."""

import pytest

from calculations.shunting_yard_algorithm import infix_to_postfix, postfix_eval
from calculations.either import Either


def test_short_expression1():
    expression1 = "1 + 2"
    postfix_expression1 = "12+"

    expression2 = "1 * 2"
    postfix_expression2 = "12*"

    expression3 = "1 / 2"
    postfix_expression3 = "12/"

    assert infix_to_postfix(expression1) == postfix_expression1
    assert infix_to_postfix(expression2) == postfix_expression2
    assert infix_to_postfix(expression3) == postfix_expression3


def test_short_expression2():
    expression1 = "1 + 2 * 3"
    postfix_expression1 = "123*+"

    expression2 = "1 * 2 + 3"
    postfix_expression2 = "12*3+"

    expression3 = "1 / 2 + 4"
    postfix_expression3 = "12/4+"

    assert infix_to_postfix(expression1) == postfix_expression1
    assert infix_to_postfix(expression2) == postfix_expression2
    assert infix_to_postfix(expression3) == postfix_expression3


def test_short_expression3():
    expression1 = "1 + 2 + 3"
    postfix_expression1 = "12+3+"

    expression2 = "1 * 2 * 3"
    postfix_expression2 = "12*3*"

    expression3 = "1 / 2 / 4"
    postfix_expression3 = "12/4/"

    assert infix_to_postfix(expression1) == postfix_expression1
    assert infix_to_postfix(expression2) == postfix_expression2
    assert infix_to_postfix(expression3) == postfix_expression3


def test_short_expression4():
    expression1 = "(1+2) * 3"
    postfix_expression1 = "12+3*"

    expression2 = "1 * ( 2 * 3 )"
    postfix_expression2 = "123**"

    assert infix_to_postfix(expression1) == postfix_expression1
    assert infix_to_postfix(expression2) == postfix_expression2


def test_long_expression1():
    expression1 = "5*8*(2+9)+(7-5+8-9*(5*5)+5)"
    postfix_expression1 = "58*29+*75-8+955**-5++"

    expression2 = "(5+1) * (10 + 2 * (3 + 4))"
    postfix_expression2 = "51+10234+*+*"

    assert infix_to_postfix(expression1) == postfix_expression1
    assert infix_to_postfix(expression2) == postfix_expression2


def test_postfix_eval():
    postfix_expression1 = "123**"
    postfix_expression1_result = 6

    postfix_expression2 = "12+3*"
    postfix_expression2_result = 9

    postfix_expression3 = "12+3+"
    postfix_expression3_result = 6

    postfix_expression4 = "12*3*"
    postfix_expression4_result = 6

    assert postfix_eval(postfix_expression1).get_right() == postfix_expression1_result
    assert postfix_eval(postfix_expression2).get_right() == postfix_expression2_result
    assert postfix_eval(postfix_expression3).get_right() == postfix_expression3_result
    assert postfix_eval(postfix_expression4).get_right() == postfix_expression4_result


def test_postfix_eval_bad():
    postfix_expression1 = "12$"
    postfix_expression2 = "1 2 3*"
    postfix_expression3 = "12+*"

    assert postfix_eval(postfix_expression1).is_left is True
    assert postfix_eval(postfix_expression2).is_left is True
    assert postfix_eval(postfix_expression3).is_left is True
