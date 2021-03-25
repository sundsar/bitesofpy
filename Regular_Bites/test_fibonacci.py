from fibonacci import fib
import pytest

# write one or more pytest functions below, they need to start with test_


def test_negative_num():
    with pytest.raises(ValueError):
        fib(-6)


def test_positive_num():
    assert fib(6) == 8


def test_zero_one():
    assert fib(0) == 0
    assert fib(1) == 1
