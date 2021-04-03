
"""
This file contains the documentation for equation.py
"""

# LinearEquation(loc, rhs):
#    A LinearEquation contains the coefficients and RHS of a linear equation
#    LinearEquation: a.sub(1)x1 + a.sub(2)x2 + ... a.sub(n)xn = rhs
#    :param loc: the list of coefficients
#    :param rhs: the right-hand-side of the equation
#
#  FIELDS:
#   * a: Vector which contains the coefficients
#   * n: number of coefficients
#   * rhs: the right-hand-side of the equation
#
#  METHODS:
#   * copy() produces a copy of self


# LinearSystem(*args):
#    A LinearSystem contains multiple LinearEquations
#    :param args: args is a list of LinearEquations
#
#  FIELDS:
#   * e: e[i] represents equation i, of the system of equations
#        e[0] is None
#   * m: m is the number of equations in the system
#   * n: is the number of unknowns in each equation


# ERO(t, instr):
#    An ERO contains the information for a specific elementary operation of a LinearSystem
#    :param t: can be 1, 2 or 3
#    :param instr: list of numbers which describe the operation, as described below
#       if t = 1: instr = [i, j], i.e., interchange equations i and j
#       if t = 2: instr = [i, k], i.e., scale equation i by k
#              note: k != 0
#       if t = 1: instr = [i, j, c], i.e., add c * equation j to equation i
#              note: i != j
#
#  FIELD:
#   * t: t is the type of the ERO (1, 2 or 3)
#   * instr: the values which describe the operation (see above)


# add(le1, le2, *args) produces the sum of le1, le2 and args

# negate(le) produces -le

# subtract(le1, le2) produces the difference le1 - le2

# scalar_multiply(le, s) scales the coefficients of le by s, modifies le

# solves_equation(le, v) produces true if v is a solution to the LinearEquation

# solves_system(ls, v) produces true if v is a solution to the LinearSystem

# equations_are_identical(le1, le2) produces true if le1 and le2 are identical

# systems_are_identical(ls1, ls2) produces true if ls1 and ls2 are identical

# apply_ero(ls, ero) applies ero to ls, modifies ls






























