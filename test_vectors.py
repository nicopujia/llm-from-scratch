import pytest

from vectors import Vector


@pytest.fixture
def v():
    return Vector(3, 4)


@pytest.fixture
def w():
    return Vector(-1, 2)


def test_addition(v, w):
    assert v + w == w + v == Vector(2, 6)


def test_cannot_add_vectors_of_different_dimensions(v):
    with pytest.raises(ValueError):
        _nonsense = v + Vector(1, 2, 3)


@pytest.mark.parametrize(
    "scalar, expected_vector",
    [
        (0, Vector(0, 0)),
        (1, Vector(3, 4)),
        (-1, Vector(-3, -4)),
        (4, Vector(12, 16)),
        (-4, Vector(-12, -16)),
        (-1.5, Vector(-4.5, -6)),
    ],
)
def test_scalar_multiplication(v, scalar: float, expected_vector: Vector):
    assert v * scalar == scalar * v == expected_vector
