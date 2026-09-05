from collections.abc import Sequence


class InvalidVectorOperation(Exception): ...


class Vector:
    def __init__(self, *values: float) -> None:
        self.dimensions = len(values)
        self.values = values

    def __repr__(self) -> str:
        str_values = " ".join([f"{value:.2f}" for value in self.values])
        return f"[ {str_values} ]"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.values == other.values

    def __add__(self, other: "Vector") -> "Vector":
        if self.dimensions != other.dimensions:
            raise InvalidVectorOperation("Cannot add vectors of different dimensions.")
        new_values = []
        for self_value, other_value in zip(self.values, other.values):
            new_values.append(self_value + other_value)
        return self.__class__(*new_values)

    def __mul__(self, arg) -> "Vector":
        match arg:
            case int() | float():
                scalar = arg
                return self.__class__(*[value * scalar for value in self.values])
            case Vector():
                raise NotImplementedError(
                    "I haven't learned vector multiplication by another vector yet."
                )
            case _:
                return NotImplemented

    def __rmul__(self, arg) -> "Vector":
        return self.__mul__(arg)

    @classmethod
    def zero(cls, dimensions: int) -> "Vector":
        return cls(*[0] * dimensions)

    @staticmethod
    def linearly_combine(
        vectors: Sequence["Vector"], scalars: Sequence[float]
    ) -> "Vector":
        if not vectors or not scalars:
            raise InvalidVectorOperation(
                "Cannot linearly combine empty sequence of vectors or scalars."
            )
        if len(vectors) != len(scalars):
            raise InvalidVectorOperation(
                "`vectors` and `scalars` must have the same length."
            )
        acc = Vector.zero(vectors[0].dimensions)
        for vector, scalar in zip(vectors, scalars):
            acc += vector * scalar
        return acc
