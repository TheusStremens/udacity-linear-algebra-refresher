import pytest

from udacity.vector import Vector


@pytest.fixture
def vector_v():
    return Vector([8.222, -9.222])


@pytest.fixture
def vector_w():
    return Vector([-1.111, 2.111])


def test_plus(vector_v, vector_w):
    assert vector_v.plus(vector_w) == Vector([7.111, -7.111])


def test_minus(vector_v, vector_w):
    assert vector_v.minus(vector_w) == Vector([9.333, -11.333])


def test_times_scalar(vector_v):
    assert vector_v.times_scalar(2.0) == Vector([16.444, -18.444])
