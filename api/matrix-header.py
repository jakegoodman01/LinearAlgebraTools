
"""
This file contains the documentation for matrix.py
"""

# Matrix(ls):
#    A Matrix emulates the interface of a matrix, which is really just a linear system of equations
#    :param ls: the LinearSystem representation of the matrix
#
#  FIELDS:
#   * ls: the LinearSystem representation of the matrix
#   * augmented: true means this is an augmented matrix, false otherwise
#   * m: number of rows
#   * n: number of columns
#
#  METHODS:
#   * copy() produces a copy of self
#   * sub(i, j) produces the the value at coordinates (i,j) of the matrix
#   * set(i, j, value) sets the value at coordinates (i,j) to value
#   * aug(k) produces the kth component of the augmented vector
#   * aug_set(k, value) sets the kth component of the augmented vector to value
#   * augment_with(b) sets the augmented column to b
#   * row(i) produces the ith row vector
#   * col(i) produces the ith column vector
#   * get_b() produces the vector b, which is the augmented column

# SuperAugmentedMatrix(rhs, lhs):
#     A SuperAugmentedMatrix represents a system of linear equations with multiple
#     potential solutions
#     :param lhs: the coefficient matrix, not augmented
#     :param rhs: the augmentation matrix, not augmented
#
#  FIELDS:
#   * lhs: the coefficient matrix
#   * rhs: the augmentation matrix
#   * m: number of rows
#   * n: number of columns (in rhs)

# zero_matrix(m, n) produces an m*n zero matrix

# matrix_equal(A, B) produces true if A and B are identical matrices

# matrix_add(A, B) produces the sum of A and B

# matrix_negate(A) produces -A

# matrix_subtract(A, B) produces A - B

# matrix_scalar_product(A, c) produces cA

# create_matrix(grid) produces a matrix with the coordinates given in grid (2d-array)

# matrix_from_columns(cols) produces a matrix composed of the column vectors given in cols

# apply_ero(A, ero) applies ero to matrix A, modifies A

# to_rref(A) uses the Canonical-Gauss-Jordan algorithm to convert A into its RREF
#  requires: the first column is not the zero vector

# rank(A) produces the rank of A

# is_consistent(A) produces true if A is consistent

# nullity(A) produces the nullity of A

# homogeneous(A) produces the equivalent homogeneous system of A

# matrix_vector_product(A, v) produces the matrix vector product, Av

# col_space(A) produces the column space of A, i.e., Col(A)

# has_solution(A, b) produces true if there is a solution to the
#  equation Ax = b, for some vector x

# identity(n) produces the identity matrix in n*n space

# matrix_transpose(A) produces the transpose of A
