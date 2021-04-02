
from typing import List
from math import acos, cos, sqrt

"""-------------------COMPLEX NUMBER STUFF---------------------"""


# conj(z) produces the conjugate of z
def conj(z: complex) -> complex:
    return complex(z.real, -z.imag)


# modulus(z) produces the modulus of z
def modulus(z: complex) -> float:
    arg = z * conj(z)  # note that arg will be real
    assert arg.imag == 0
    return sqrt(arg.real)


"""------------------------VECTOR STUFF------------------------"""

TOLERANCE = 0.0001


class Vector:
    def __init__(self, *args):
        self.components = []
        self.field = 'real'
        for i in args:
            self.components.append(i)
            if isinstance(i, complex):
                self.field = 'complex'
        self.dim = len(self.components)
        assert self.dim > 0, "Empty Coordinates List"

    def __repr__(self):
        output = f'[{self.components[0]}'
        for i in range(1, self.dim):
            output += f', {self.components[i]}'
        output += ']'
        return output

    # zero_vector() produces the zero_vector in the same dimension as self
    def zero_vector(self):
        zeros = [0] * self.dim
        return Vector(*zeros)

    # is_zero() produces true if self is the zero vector
    def is_zero(self):
        return is_equal(self, self.zero_vector())

    # copy() produces a copy of self
    def copy(self):
        return Vector(*self.components)


# vector_equals(v, w) produces true if v equals w
def is_equal(v: Vector, w: Vector) -> bool:
    if v.dim == w.dim:
        for i in range(v.dim):
            if abs(v.components[i] - w.components[i]) > TOLERANCE:
                return False
        return True
    return False


# vector_add(v, w, *args) produces the sum of v, w and args
# requires: v and w are in the same dimension
def add(v: Vector, w: Vector, *args: Vector) -> Vector:
    assert v.dim == w.dim, "Can't add vectors of different dimensions"
    new_vector = v.zero_vector()
    for i in range(v.dim):
        new_vector.components[i] = v.components[i] + w.components[i]
    for vector in args:
        new_vector = add(new_vector, vector)
    return new_vector


# vector_negate(v) produces -v
def negate(v: Vector) -> Vector:
    new_vector = v.zero_vector()
    for i in range(v.dim):
        new_vector.components[i] -= v.components[i]
    return new_vector


# vector_subtract(v, w) produces the difference v - w
# requires: v and w are in the same dimension
def subtract(v: Vector, w: Vector) -> Vector:
    return add(v, negate(w))


# vector_scalar_multiply(v, s) produces the product of v and s
def scalar_multiply(v: Vector, s) -> Vector:
    if isinstance(s, complex):
        assert v.field == 'complex', "Can't multiply a real vector by a complex number"
    new_vector = v.copy()
    for i in range(v.dim):
        new_vector.components[i] *= s
    return new_vector


# dot_product(v, w) produces the dot product of v and w
# requires: v and w are in the same dimension
def dot_product(v: Vector, w: Vector):
    assert v.dim == w.dim, "Can't dot vectors of different dimensions"
    result = 0
    for i in range(v.dim):
        result += v.components[i] * w.components[i]
    return result


# norm(v) produces the length (or norm) of v
def norm(v: Vector) -> float:
    if v.field == 'complex':
        arg = inner_product(v, v)
        assert arg.imag == 0
        return sqrt(inner_product(v, v).real)
    return sqrt(dot_product(v, v))


# normalize(v) produces v normalized
def normalize(v: Vector) -> Vector:
    return scalar_multiply(
        v,
        1 / norm(v)
    )


# is_orthogonal(v, w) produces true of v and w are orthogonal
def is_orthogonal(v: Vector, w: Vector) -> bool:
    return dot_product(v, w) == 0


# angle(v, w) produces the angle, in radians [0, pi], between v and w
def angle(v: Vector, w: Vector) -> float:
    dot = dot_product(v, w)
    arg = dot / (norm(v) * norm(w))
    return acos(arg)


# proj(v, w) produces the projection of v along w
def proj(v: Vector, w: Vector) -> Vector:
    if v.field == 'real' and w.field == 'real':
        dot = dot_product(v, w)
        scalar = dot / (norm(w) ** 2)
        return scalar_multiply(w, scalar)
    elif v.field == 'complex' and w.field == 'complex':
        dot = inner_product(v, w)
        scalar = dot / (norm(w) ** 2)
        return scalar_multiply(w, scalar)
    else:
        assert False, "Cannot project complex and real vectors"


# component(v, w) produces the component of v along w
# requires: w != 0
def component(v: Vector, w: Vector) -> float:
    assert not w.is_zero(), "w is zero"
    return norm(v) * cos(angle(v, w))


# perp(v, w) produces the remainder of v along w, a.k.a. perp
# requires: w != 0
def perp(v: Vector, w: Vector) -> Vector:
    assert not w.is_zero(), "w is zero"
    return subtract(v, proj(v, w))


# vector_conj(v) produces the conjugate of vector v
def vector_conj(v: Vector) -> Vector:
    new_vector = v.copy()
    for i in range(new_vector.dim):
        new_vector.components[i] = conj(new_vector.components[i])
    return new_vector


# inner_product(w, z) produces the standard inner product <w, z>
def inner_product(w: Vector, z: Vector) -> complex:
    return dot_product(w, vector_conj(z))






