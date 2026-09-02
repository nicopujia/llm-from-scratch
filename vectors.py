class Vector:
    def __init__(self, *values: float) -> None:
        self.dimensions = len(values)
        self.values = values

    def __repr__(self) -> str:
        str_values = " ".join([f"{value:.2f}" for value in self.values])
        return f"[ {str_values} ]"

    def __eq__(self, other) -> bool:
        return (
            isinstance(self, Vector)
            and isinstance(other, Vector)
            and self.values == other.values
        )

    def __add__(self, other: "Vector") -> "Vector":
        if self.dimensions != other.dimensions:
            raise ValueError("Cannot add vectors of different dimensions.")
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
                raise TypeError(
                    "Invalid vector multiplication. You have to multiply a vector either by a scalar or by another vector."
                )

    def __rmul__(self, arg) -> "Vector":
        return self.__mul__(arg)
