
"""
This file contains the documentation for space.py
"""


# Span(*args):
#    A Span object represents the Span of the the given vectors in args
#    Span = {a1v1 + a2v2 + ... + apvp : a1, a1, ..., ap e F}
#    :param args: the spanning vectors
#
#  FIELDS:
#   * vectors: the normalized vectors which define the span


# Line(v, w):
#    A Line object represents a line in (v.dim) dimensional space
#    Line = {v + tw: t e F}
#    :param v: the "starting point" of the line
#    :param w: the direction of the line
#    requires: v and w are in the same field and dimension
#              w is not the zero vector
#
#  FIELDS:
#   * v: the "starting point" of the line
#   * w: the direction of the line
#   * field: the field of the line


# Plane(p, v, w):
#    A Plane object represents a plane in (v.dim) dimensional space
#    Plane = {p + sv + tw: s,t e F}
#    :param p: the "starting point" of the plane
#    :param v: the first direction of the plane
#    :param w: the second direction of the plane
#    requires: p, v and w are in the same field and dimension
#              v and w are both not the zero vector
#              v and w are not co-linear
#
#  FIELDS:
#   * p: the "starting point" of the plane
#   * v: the first direction of the plane
#   * w: the second direction of the plane
#   * field: the field of the plane


# span_is_equal(S, U) produces true if S and U are equal Spans

# contained_in_span(v, S) produces true if v is in the Span S

# line_passing_through(v, w) produces a Line which passes through the terminal points
#  of v and w
#  requires: v and w must be in the same field and dimension
#            w cannot be the zero vector

# lies_on_line(L, v) produces true if the terminal point of v lies on the Line L

# line_is_equal(L, Y) produces true if the Lines L and Y represent the same Line

# plane_passing_through(p, r, q) produces a Plane which passes through the terminal points
#  of p, r and q
#  requires: p, r and q must be in the same field and dimension
#           (q - p) must not be co-linear with (r - p)

# lies_on_plane(P, v) produces true if the terminal point of v lies on the Plane P

# plane_is_equal(P, Y) produces true if the Planes P and Y represent the same Plane



