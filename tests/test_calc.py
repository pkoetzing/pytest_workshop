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
    'actual, expected',
    [
        ('100, 90', 10),
        ('-10, -2', -8),
        ('0, -8', 8),
        ('100, 11, 7, 21', 61),
        pytest.param("100, 90", 42, marks=pytest.mark.xfail)
    ])
def test_sub(actual, expected):
    '''Test "corner cases" of sub function'''
    c = Calc()
    act = tuple(map(int, actual.split(',')))
    assert c.sub(*act) == expected
