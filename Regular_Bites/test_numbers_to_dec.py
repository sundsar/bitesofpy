import pytest

from numbers_to_dec import list_to_decimal


def test_outofrange():
    with pytest.raises(ValueError):
        list_to_decimal([5, 10])


def test_negativenum():
    with pytest.raises(ValueError):
        list_to_decimal([5, -10])


def test_boolInstance():
    with pytest.raises(TypeError):
        list_to_decimal([5, True])


def test_notintInstance():
    with pytest.raises(TypeError):
        list_to_decimal([5, '3'])
        list_to_decimal([5, 3.3])
        list_to_decimal([5, (1, 2)])
        list_to_decimal([5, [1, 2]])
        list_to_decimal([5, {'a': 1, 'b': 2}])
        list_to_decimal({'a': 1, 'b': 2})
        list_to_decimal('123')


def test_valid():
    assert list_to_decimal([0, 4, 2, 8]) == 428
    assert list_to_decimal([1, 2]) == 12
    assert list_to_decimal([3]) == 3
