#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pytest_workshop
----------------------------------

Tests for `pytest_workshop` module.
"""

from pytest_workshop.calc import Calc


def test_add_two_numbers():
    c = Calc()
    assert c.add(4, 5) == 9


def test_add_three_numbers():
    c = Calc()
    assert c.add(4, 5, 6) == 15


def test_add_many_numbers():
    c = Calc()
    assert c.add(*range(100)) == 4950
