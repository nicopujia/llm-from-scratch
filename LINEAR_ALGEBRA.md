# Linear Algebra

This document has notes taken from the free course [Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab), by [3Blue1Brown](https://www.youtube.com/@3blue1brown).

## [Chapter 1](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=1&t=338s): Vectors

There are 3 perspectives of what vectors are:

- **Physics**: arrows or movement in space
- **CS**: ordered lists of numbers
- **Math**: a "mix" of physics and CS, focusing mostly on the fact that these entities (ie vectors) can be added and multiplied

In linear algebra, they're conventionally written with vertically and with square brackets instead of horizontally and with parenthesis to differenciate them from coordinates.

### Addition

*Physics-like method*: for adding vector `v` + vector `w`, put `v`'s "tail" in `w`'s "head", then draw a new vector from `w`'s "tail" to `v`'s "head", and that's the result of the addition. The same can be done interchangeably with `v` and `w`—the order doesn't matter. A vector, let's say `[-2, 3]`, can be understood as "take 2 steps to the left, then 3 up."

*CS-like method*: add each number of the vector by the corresponding of the other vector, ie `[A, B] + [C, D] = [A+C, B+D]`.

Both methods are equivalent because they mean the same thing, just represented differently. This is what the math perspective refers to: that whether you visualize the vectors or you process them as lists, they're the same thing in the end, and adding/multiplying them is the same operation, and only the way you represent them changes.

### Scaling

A scalar is a single number. Scaling a vector means multiplying it by a scalar. By doing so, you can "stretch" or "shrink" the vector. To scale a vector, multiply each vector number by the scalar, ie `[A, B] * C = [A*C, B*C]`
