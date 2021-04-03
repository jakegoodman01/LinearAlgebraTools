
from typing import List
from math import acos, cos, sqrt


def conj(z: complex) -> complex:
    return complex(z.real, -z.imag)


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

    def zero_vector(self):
        zeros = [0] * self.dim
        return Vector(*zeros)

    def is_zero(self):
        return is_equal(self, self.zero_vector())

    def copy(self):
        return Vector(*self.components)

    def sub(self, n):
        assert 1 <= n <= self.dim, "Invalid component request"
        return self.components[n - 1]


def is_equal(v: Vector, w: Vector) -> bool:
    if v.dim == w.dim:
        for i in range(v.dim):
            if abs(v.components[i] - w.components[i]) > TOLERANCE:
                return False
        return True
    return False


def add(v: Vector, w: Vector, *args: Vector) -> Vector:
    assert v.dim == w.dim, "Can't add vectors of different dimensions"
    new_vector = v.zero_vector()
    for i in range(v.dim):
        new_vector.components[i] = v.components[i] + w.components[i]
        if isinstance(new_vector.components[i], complex):
            new_vector.field = 'complex'
    for vector in args:
        new_vector = add(new_vector, vector)
    return new_vector


def negate(v: Vector) -> Vector:
    new_vector = v.zero_vector()
    for i in range(v.dim):
        new_vector.components[i] -= v.components[i]
    return new_vector


def subtract(v: Vector, w: Vector) -> Vector:
    return add(v, negate(w))


def scalar_multiply(v: Vector, s) -> Vector:
    if isinstance(s, complex):
        assert v.field == 'complex', "Can't multiply a real vector by a complex number"
    new_vector = v.copy()
    for i in range(v.dim):
        new_vector.components[i] *= s
    return new_vector


def is_scalar_multiple(v: Vector, w: Vector) -> bool:
    assert v.dim == w.dim, "v and w are not in the same dimension"
    if v.is_zero() or w.is_zero():
        return True
    m = 0  # m is the scaling factor, to satisfy v = mw
    for i in range(1, v.dim + 1):
        if v.sub(i) == w.sub(i) == 0:
            pass
        elif v.sub(i) != 0 and w.sub(i) != 0:
            if m == 0:
                m = v.sub(i) / w.sub(i)
            elif abs(v.sub(i) / w.sub(i) - m) > TOLERANCE:
                return False
        else:
            return False
    assert m != 0, "Something went wrong..."
    print(m)
    return True


def dot_product(v: Vector, w: Vector):
    assert v.dim == w.dim, "Can't dot vectors of different dimensions"
    result = 0
    for i in range(v.dim):
        result += v.components[i] * w.components[i]
    return result


def norm(v: Vector) -> float:
    if v.field == 'complex':
        arg = inner_product(v, v)
        assert arg.imag == 0
        return sqrt(inner_product(v, v).real)
    return sqrt(dot_product(v, v))


def normalize(v: Vector) -> Vector:
    return scalar_multiply(v, 1 / norm(v))


def is_orthogonal(v: Vector, w: Vector) -> bool:
    return dot_product(v, w) == 0


def angle(v: Vector, w: Vector) -> float:
    dot = dot_product(v, w)
    arg = dot / (norm(v) * norm(w))
    return acos(arg)


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


def component(v: Vector, w: Vector) -> float:
    assert not w.is_zero(), "w is zero"
    return norm(v) * cos(angle(v, w))


def perp(v: Vector, w: Vector) -> Vector:
    assert not w.is_zero(), "w is zero"
    return subtract(v, proj(v, w))


def vector_conj(v: Vector) -> Vector:
    new_vector = v.copy()
    for i in range(new_vector.dim):
        new_vector.components[i] = conj(new_vector.components[i])
    return new_vector


def inner_product(w: Vector, z: Vector) -> complex:
    return dot_product(w, vector_conj(z))


def cross_product(u: Vector, v: Vector) -> Vector:
    assert u.field == 'real' and v.field == 'real', "u and v must be real vectors"
    assert u.dim == 3 and v.dim == 3, "u and v must be in 3-dimensions"
    return Vector(
        u.sub(2) * v.sub(3) - u.sub(3) * v.sub(2),
        -(u.sub(1) * v.sub(3) - u.sub(3) * v.sub(1)),
        u.sub(1) * v.sub(2) - u.sub(2) * v.sub(1)
    )



