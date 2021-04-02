
from typing import List

"""------------------------VECTOR STUFF------------------------"""


class Vector:
    def __init__(self, nums: List[int]):
        self.dim = len(nums)
        assert self.dim > 0, "Empty Coordinates List"
        self.components = nums

    def __repr__(self):
        output = f'(\n {self.components[0]},\n'
        for i in range(1, self.dim):
            output += f' {self.components[i]},\n'
        output += ')'
        return output

    # zero_vector() produces the zero_vector in the same dimension as self
    # time: O(1)
    def zero_vector(self):
        zero = Vector([0] * self.dim)
        return zero

    # is_zero() produces true if self is the zero vector
    # time: O(n)
    def is_zero(self):
        return vector_equals(self, self.zero_vector())

    # copy() produces a copy of self
    def copy(self):
        new_vector = self.zero_vector()
        for i in range(self.dim):
            new_vector.components[i] = self.components[i]
        return new_vector


# vector_equals(v, w) produces true if v equals w
# time: O(n)
def vector_equals(v: Vector, w: Vector) -> bool:
    if v.dim == w.dim:
        for i in range(v.dim):
            if v.components[i] != w.components[i]:
                return False
        return True
    return False


# vector_add(v, w, *args) produces the sum of v, w and args
# requires: v and w are in the same dimension
# time: O(n)
def vector_add(v: Vector, w: Vector, *args: Vector) -> Vector:
    assert v.dim == w.dim, "Can't add vectors of different dimensions"
    new_vector = v.zero_vector()
    for i in range(v.dim):
        new_vector.components[i] = v.components[i] + w.components[i]
    for vector in args:
        new_vector = vector_add(new_vector, vector)
    return new_vector


# vector_negate(v) produces -v
# time: O(n)
def vector_negate(v: Vector) -> Vector:
    new_vector = v.zero_vector()
    for i in range(v.dim):
        new_vector.components[i] -= v.components[i]
    return new_vector


# vector_subtract(v, w) produces the difference v - w
# requires: v and w are in the same dimension
# time: O(n)
def vector_subtract(v: Vector, w: Vector) -> Vector:
    return vector_add(v, vector_negate(w))


# vector_scalar_multiply(v, s) produces the product of v and s
# time: O(n)
def vector_scalar_multiply(v: Vector, s: int) -> Vector:
    new_vector = v.copy()
    for i in range(v.dim):
        new_vector.components[i] *= s
    return new_vector


# dot_product(v, w) produces the dot product of v and w
# requires: v and w are in the same dimension
# time: O(n)
def dot_product(v: Vector, w: Vector):
    assert v.dim == w.dim, "Can't dot vectors of different dimensions"
    result = 0
    for i in range(v.dim):
        result += v.components[i] * w.components[i]
    return result












