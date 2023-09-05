import pytest


def test_greater():
    num = 100
    assert num > 100


def test_greater_equal():
    num = 100
    assert num >= 100


def test_less():
    num = 100
    assert num < 200


@pytest.mark.group1
def test_group1():
    num = 100
    assert num < 200


@pytest.mark.group2
def test_group2():
    num = 100
    assert num < 200
