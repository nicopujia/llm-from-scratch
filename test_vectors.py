import pytest

from vectors import InvalidVectorOperation, Vector


@pytest.fixture
def v():
    return Vector(3, 4)


@pytest.fixture
def w():
    return Vector(-1, 2)


def test_addition(v, w):
    assert v + w == w + v == Vector(2, 6)


def test_cannot_add_vectors_of_different_dimensions(v):
    with pytest.raises(InvalidVectorOperation):
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


@pytest.mark.parametrize(
    "vectors, scalars, linear_combination",
    [
        ([Vector(1, 0), Vector(0, 1)], [2, 3], Vector(2, 3)),
        ([Vector(2, 0), Vector(0, 1)], [2, 3], Vector(4, 3)),
        ([Vector(0, 0), Vector(0, 0)], [2, 3], Vector(0, 0)),
        ([Vector(2, 1), Vector(4, 2)], [2, 3], Vector(16, 8)),
        (
            [Vector(2, 0, 0), Vector(0, 1, 0), Vector(0, 0, 1.5)],
            [5, 3, 8],
            Vector(10, 3, 12),
        ),
        (
            [Vector(1, 0, 0), Vector(0, 1, 0), Vector(1, 1, 0)],
            [2, 3, 0],
            Vector(2, 3, 0),
        ),
        (
            [Vector(1, 0, 0), Vector(0, 1, 0), Vector(1, 1, 0)],
            [0, 1, 2],
            Vector(2, 3, 0),
        ),
    ],
)
def test_linear_combinations(vectors, scalars, linear_combination):
    assert linear_combination == Vector.linearly_combine(vectors, scalars)


@pytest.mark.parametrize(
    "vectors, scalars",
    [
        ([Vector(0, 0), Vector(0, 0)], [0]),
        ([Vector(0, 0)], [0, 0]),
        ([Vector(0, 0)], []),
        ([], [0]),
        ([], []),
    ],
)
def test_cant_linearly_combine_diff_or_empty_seq_len(vectors, scalars):
    with pytest.raises(InvalidVectorOperation):
        _nonsense = Vector.linearly_combine(vectors, scalars)


def test_cant_linearly_combine_vectors_of_diff_dimensions():
    with pytest.raises(InvalidVectorOperation):
        _nonsense = Vector.linearly_combine([Vector(1, 0), Vector(0, 1, 0)], [0, 0])
