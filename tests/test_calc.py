#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pytest_workshop
----------------------------------

Tests for `pytest_workshop` module.
"""

import pytest

from pytest_workshop.calc import Calc


def test_add_two_numbers():
    c = Calc()
    assert c.add(4, 5) == 9


def test_add_many_numbers():
    c = Calc()
    assert c.add(*range(100)) == 4950


def test_sub_two_numbers():
    c = Calc()
    assert c.sub(10, 3) == 7


def test_sub_many_numbers():
    c = Calc()
    assert c.sub(100, 11, 7, 21) == 61


@pytest.mark.parametrize(
    'act, exp',
    [
        ((100, 90), 10),
        ((-10, -2), -8),
        ((0, -8), 8),
        ((100, 11, 7, 21), 61),
    ])
def test_sub(act, exp):
    '''Test "corner cases" of sub function'''
    c = Calc()
    assert c.sub(*act) == exp


def test_multiply_two_numbers():
    c = Calc()
    assert c.mul(4, 6) == 24


@pytest.mark.parametrize(
    'act, exp',
    [
        ((4, 6), 24),
        ((-3, -5), 15),
        (range(1, 10), 362880)
    ])
def test_mul(act, exp):
    '''Test "corner cases" of mul function'''
    c = Calc()
    assert c.mul(*act) == exp


def test_multiply_by_zero_exception():
    with pytest.raises(ValueError):
        c = Calc()
        c.mul(1, 0)


def test_divide_two_numbers():
    c = Calc()
    assert c.div(8, 4) == 2


@pytest.mark.parametrize(
    'act, exp',
    [
        ((11, 2), 5.5),
        ((-9, -3), 3),
        ((1, 3), 0.333),
        ((100, 10, 0), float('inf')),
    ])
def test_div(act, exp):
    '''Test "corner cases" of mul function'''
    c = Calc()
    assert c.div(*act) == pytest.approx(exp, rel=0.01)


def test_average_iterable():
    c = Calc()
    assert c.avg([2, 5, 12, 98]) == 29.25


def test_average_outliers():
    c = Calc()
    assert c.avg(
        [2, 5, 12, 98], lower=0, upper=50) == pytest.approx(6.333, rel=0.01)


def test_average_zero_limit():
    c = Calc()
    assert c.avg([-1, 0, 1], lower=0) == 0.5


def test_average_empty_iterable():
    c = Calc()
    with pytest.raises(ZeroDivisionError):
        c.avg([])


def test_average_non_iterable():
    c = Calc()
    with pytest.raises(TypeError):
        c.avg(123)
