'''
Tests for `calc` module.
'''

import pytest

from pytest_tdd import calc


# Addition
def test_add_two_numbers():
    assert calc.add(4, 5) == 9


def test_add_many_numbers():
    assert calc.add(*range(100)) == 4950


@pytest.mark.parametrize(
    'act, exp',
    [
        ((-10, -2), -12),
        ((0, -8), -8),
        ((), 0)
    ])
def test_add(act, exp):
    '''Test "corner cases" of add function'''
    assert calc.add(*act) == exp

# Subtraction
@pytest.mark.parametrize(
    'act, exp',
    [
        ((100, 90), 10),
        ((-10, -2), -8),
        ((0, -8), 8),
    ])
def test_sub(act, exp):
    '''Test "corner cases" of sub function'''
    assert calc.sub(*act) == exp


# Multiplication
def test_multiply_two_numbers():
    assert calc.mul(4, 6) == 24


@pytest.mark.parametrize(
    'act, exp',
    [
        ((4, 6), 24),
        ((-3, -5), 15),
        (range(1, 10), 362880)
    ])
def test_mul(act, exp):
    '''Test "corner cases" of mul function'''
    assert calc.mul(*act) == exp


def test_multiply_by_zero_exception():
    with pytest.raises(ValueError):
        calc.mul(1, 0)


# Division
def test_divide_two_numbers():
    assert calc.div(8, 4) == 2


@pytest.mark.parametrize(
    'act, exp',
    [
        ((11, 2), 5.5),
        ((-9, -3), 3),
        ((1, 3), 0.333),
        ((10, 0), float('inf')),
    ])
def test_div(act, exp):
    '''Test "corner cases" of mul function'''
    assert calc.div(*act) == pytest.approx(exp, rel=0.01)


# Averaging
def test_average_iterable():
    assert calc.avg([2, 5, 12, 98]) == 29.25


def test_average_outliers():
    assert calc.avg([2, 5, 12, 98],
                    lower_bound=0,
                    upper_bound=50) == pytest.approx(6.333, rel=0.01)


def test_average_zero_limit():
    assert calc.avg([-1, 0, 1], lower_bound=0) == 0.5


def test_average_empty_iterable():
    with pytest.raises(ZeroDivisionError):
        calc.avg([])


def test_average_non_iterable():
    with pytest.raises(TypeError):
        calc.avg(123)
