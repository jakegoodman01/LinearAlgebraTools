
from typing import List
from api import equation as eq
from api import vector as vc


class Matrix:
    def __init__(self, ls: eq.LinearSystem):
        self.ls = ls
        self.augmented = False
        self.m = ls.m
        self.n = ls.n

    def __repr__(self):
        width = 6
        decimals = 3
        output = ''
        for i in range(1, self.m + 1):
            output += '[ '
            for j in range(1, self.n + 1):
                if abs(self.sub(i, j)) < vc.TOLERANCE:
                    output += f'{0:^{width}.{decimals}g}'
                elif isinstance(self.sub(i, j), complex):
                    output += f'{vc.format_complex(self.sub(i, j)):^{width}}'
                else:
                    output += f'{self.sub(i, j):^{width}.{decimals}g}'
            if self.augmented:
                if abs(self.aug(i)) < vc.TOLERANCE:
                    output += f' | {0:^{width}.{decimals}g}'
                elif isinstance(self.aug(i), complex):
                    output += f' | {vc.format_complex(self.aug(i)):^{width}}'
                else:
                    output += f' | {self.aug(i):^{width}.{decimals}g}'
            output += ' ]\n'
        return output

    def copy(self):
        return Matrix(self.ls.copy())

    def sub(self, i: int, j: int):
        row = self.ls.e[i]
        assert isinstance(row, eq.LinearEquation)
        return row.a.sub(j)

    def set(self, i: int, j: int, value):
        row = self.ls.e[i]
        assert isinstance(row, eq.LinearEquation)
        row.a.components[j - 1] = value

    def aug(self, k: int):
        assert self.augmented
        row = self.ls.e[k]
        assert isinstance(row, eq.LinearEquation)
        return row.rhs

    def aug_set(self, k: int, value):
        assert self.augmented
        row = self.ls.e[k]
        assert isinstance(row, eq.LinearEquation)
        row.rhs = value

    def augment_with(self, b: vc.Vector):
        assert b.dim == self.m
        self.augmented = True
        for i in range(1, self.m + 1):
            self.aug_set(i, b.sub(i))

    def row(self, i: int):
        assert 1 <= i <= self.m, "Invalid row request"
        return self.ls.e[i].a.copy()

    def col(self, i: int):
        assert 1 <= i <= self.n
        li = [self.sub(r, i) for r in range(1, self.m + 1)]
        return vc.Vector(*li)

    def get_b(self):
        assert self.augmented
        li = [self.ls.e[i].rhs for i in range(1, self.m + 1)]
        return vc.Vector(*li)


class SuperAugmentedMatrix:
    def __init__(self, lhs: Matrix, rhs: Matrix):
        assert rhs.m == lhs.m
        assert not lhs.augmented and not rhs.augmented
        self.rhs = rhs
        self.lhs = lhs
        self.m = lhs.m
        self.n = lhs.n

    def __repr__(self):
        width = 6
        decimals = 3
        output = ''
        for i in range(1, self.m + 1):
            output += '[ '
            for j in range(1, self.n + 1):
                if self.lhs.sub(i, j) == 0:
                    output += f'{0:^{width}.{decimals}g}'
                else:
                    output += f'{self.lhs.sub(i, j):^{width}.{decimals}g}'
            output += f' | '
            for j in range(1, self.rhs.n + 1):
                if self.rhs.sub(i, j) == 0:
                    output += f'{0:^{width}.{decimals}g}'
                else:
                    output += f'{self.rhs.sub(i, j):^{width}.{decimals}g}'
            output += ' ]\n'
        return output


def matrix_equal(A: Matrix, B: Matrix) -> bool:
    assert A.m == B.m and A.n == B.n, "Matrices have different dimensions"
    assert A.augmented == B.augmented, "One Matrix is augmented, the other is not"
    if A.augmented and vc.is_equal(A.get_b(), B.get_b()):
        return False
    for i in range(1, A.n + 1):
        if not vc.is_equal(A.col(i), B.col(i)):
            return False
    return True


def create_matrix(grid) -> Matrix:
    system = eq.LinearSystem()
    for row in grid:
        system = eq.include_equation(
            system,
            eq.LinearEquation(row, rhs=0)
        )
    return Matrix(system)


def matrix_from_columns(cols: List[vc.Vector]) -> Matrix:
    assert len(cols) > 0, "Given empty list of vectors"
    n = len(cols)
    m = cols[0].dim
    grid = []
    for i in range(1, m + 1):
        row = []
        for v in cols:
            assert v.dim == m, "Inconsistent dimensions of given cols"
            row.append(v.sub(i))
        grid.append(row)
    return create_matrix(grid)


def apply_ero(A: Matrix, ero):
    eq.apply_ero(A.ls, ero)


def to_rref(A: Matrix):
    if isinstance(A, SuperAugmentedMatrix):
        rhs_col_vectors = []
        for i in range(1, A.lhs.n + 1):
            matrix = A.lhs.copy()
            matrix.augment_with(A.rhs.col(i))
            to_rref(matrix)
            rhs_col_vectors.append(matrix.get_b())
        to_rref(A.lhs)
        A.rhs = matrix_from_columns(rhs_col_vectors)
    else:
        assert(not A.col(1).is_zero())

        def next_pivot(i, j):
            """
            next_pivot(i, j) produces the coordinates of the next pivot, after (i,j)
            modifies A so that it has a pivot at (i+1, q) if it exists, and transforms
            other entries along column q to zero
            :param i: row index
            :param j: column index
            :return: tuple(i+1, q), the next pivot, or (0,0) if it doesn't exist
            """
            # Step 4
            k = 0
            q = 0
            for col in range(j + 1, A.n + 1):
                for row in range(i + 1, A.m + 1):
                    if abs(A.sub(row, col)) > vc.TOLERANCE:
                        k = row
                        q = col
                        break
                if k > 0:
                    break
            if k == 0 or q == 0:
                return 0, 0
            if k != i + 1:
                apply_ero(A, eq.ERO(1, [i + 1, k]))
            # Step 5
            apply_ero(A, eq.ERO(2, [i + 1, 1 / A.sub(i + 1, q)]))
            # Step 6
            for m in range(1, A.m + 1):
                if m != i + 1:
                    apply_ero(A, eq.ERO(3, [m, i + 1, -1 * A.sub(m, q)]))
            return i + 1, q

        # Step 1, obtain a pivot in the (1,1) position
        i = 1
        while A.sub(i, 1) == 0:
            i += 1
        if 1 < i:
            apply_ero(A, eq.ERO(1, [1, i]))
        assert A.sub(1, 1) != 0
        # Step 2, scale row 1 by 1 / A.sub(1, 1)
        apply_ero(A, eq.ERO(2, [1, 1 / A.sub(1, 1)]))
        # Step 3, transform other entries in column 1 to zero
        for m in range(2, A.m + 1):
            apply_ero(A, eq.ERO(3, [m, 1, -1 * A.sub(m, 1)]))
        t, r = 1, 1
        while True:
            tempt, tempr = next_pivot(t, r)
            if tempt != 0:
                t, r = tempt, tempr
            else:
                break


def rank(A: Matrix) -> int:
    B = A.copy()
    to_rref(B)
    r = 0
    for m in range(1, A.m + 1):
        if A.augmented:
            if not eq.is_trivial_equation(B.ls.e[m]):
                r += 1
            else:
                break
        else:
            if not B.ls.e[m].a.is_zero():
                r += 1
            else:
                break
    return r


def is_consistent(A: Matrix) -> bool:
    B = A.copy()
    B.augmented = not A.augmented
    return rank(A) == rank(B)


def nullity(A: Matrix) -> int:
    return A.n - rank(A)


def homogeneous(A: Matrix) -> Matrix:
    B = A.copy()
    ze = A.get_b().zero_vector()
    B.augment_with(ze)
    return B


def matrix_vector_product(A: Matrix, v: vc.Vector) -> vc.Vector:
    assert not A.augmented
    assert A.n == v.dim
    cols = []
    for i in range(1, v.dim + 1):
        cols.append(vc.scalar_multiply(
            A.col(i), v.sub(i)
        ))
    assert len(cols) > 0
    if len(cols) == 1:
        return cols[0]
    else:
        return vc.add(cols[0], cols[1], *cols[2:])


def matrix_matrix_product(A: Matrix, B: Matrix):
    assert not A.augmented and not B.augmented
    assert A.n == B.m
    transformed = []
    for i in range(1, B.n + 1):
        basis = B.col(i)
        transformed_basis = matrix_vector_product(A, basis)
        transformed.append(transformed_basis)
    return matrix_from_columns(transformed)





