
"""
This file contains the documentation for vector.py
"""

# conj(z) produces the conjugate of z

# modulus(z) produces the modulus of z


# Vector(*args):
#    A Vector object represents the vector with the given coordinates in args
#    Vector = (args[0], args[1], ..., args[n])^T
#    :param args: the coordinates of the Vector
#
#  FIELDS:
#   * components: the list of the components of the vector
#   * field: the field of the vector
#   * dim: the dimension of the vector
#
#  METHODS:
#   * zero_vector() produces the zero_vector in the same dimension as self
#   * is_zero() produces true if self is the zero vector
#   * copy() produces a copy of self
#   * sub(n) produces the nth component of self
#


# is_equal(v, w) produces true if v equals w

# add(v, w, *args) produces the sum of v, w and args
#  requires: v and w are in the same dimension

# negate(v) produces -v

# subtract(v, w) produces the difference v - w
#  requires: v and w are in the same dimension

# scalar_multiply(v, s) produces the product of v and s
#  requires: v and s are in the same field

# is_scalar_multiple(v, w) produces true if v and w are scalar multiples of each other
#  requires: v and w are in the same dimension

# dot_product(v, w) produces the dot product of v and w
#  requires: v and w are in the same dimension

# norm(v) produces the length (or norm) of v

# normalize(v) produces v normalized

# is_orthogonal(v, w) produces true of v and w are orthogonal

# angle(v, w) produces the angle, in radians [0, pi], between v and w

# proj(v, w) produces the projection of v along w

# component(v, w) produces the component of v along w
#  requires: w != 0

# perp(v, w) produces the remainder of v along w, a.k.a. perp
#  requires: w != 0

# vector_conj(v) produces the conjugate of vector v

# inner_product(w, z) produces the standard inner product <w, z>

# cross_product(u, v) produces the cross product of u and v
#  requires: u and v are vectors in R^3

# extend_zeros(v, n) adds n zeros of "padding" onto the tail of v, modifies v


