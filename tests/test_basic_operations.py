import math

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


def test_constructor_fails():
    with pytest.raises(ValueError):
        Vector([])
    with pytest.raises(TypeError):
        Vector()
    with pytest.raises(TypeError):
        Vector(2.8)


def test_magnitude():
    v = Vector([-0.211, 7.437])
    w = Vector([8.813, -1.331, -6.247])
    assert math.isclose(v.magnitude(), 7.440, rel_tol=1e-3)
    assert math.isclose(w.magnitude(), 10.884, rel_tol=1e-3)


def test_normalize():
    v = Vector([5.581, -2.136])
    w = Vector([1.996, -3.108, -4.554])
    print(v.normalize())
    print(w.normalize())
    assert v.normalize() == Vector([0.934, -0.357])
    assert w.normalize() == Vector([0.340, -0.530, -0.777])
    with pytest.raises(ZeroDivisionError):
        zero_v = Vector([0.0, 0.0, 0.0])
        zero_v.normalize()


def test_dot():
    v = Vector([7.887, 4.138])
    w = Vector([-8.802, 6.776])
    assert math.isclose(v.dot(w), -41.382, rel_tol=1e-3)
    v = Vector([-5.955, -4.904, -1.874])
    w = Vector([-4.496, -8.755, 7.103])
    assert math.isclose(v.dot(w), 56.397, rel_tol=1e-3)


def test_angle():
    v = Vector([3.183, -7.627])
    w = Vector([-2.668, 5.319])
    assert math.isclose(v.angle(w), 3.072, rel_tol=1e-3)
    v = Vector([7.350, 0.221, 5.188])
    w = Vector([2.751, 8.259, 3.985])
    assert math.isclose(v.angle(w, in_degrees=True), 60.276, rel_tol=1e-3)
    with pytest.raises(Exception):
        zero_v = Vector([0.0, 0.0, 0.0])
        v.angle(zero_v)
