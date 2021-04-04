
from api import equation as eq
from api import vector as vc


class Matrix:
    def __init__(self, ls: eq.LinearSystem):
        self.ls = ls
        self.augmented = False
        self.m = ls.m
        self.n = ls.n

    def __repr__(self):
        output = ''
        for i in range(1, self.m + 1):
            output += '[ '
            for j in range(1, self.n + 1):
                output += f'{self.sub(i, j):^6.2g}'
            if self.augmented:
                output += f' | {self.aug(i):^6.2g}'
            output += ' ]\n'
        return output

    def copy(self):
        return Matrix(self.ls)

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


def create_matrix(grid) -> Matrix:
    system = eq.LinearSystem()
    for row in grid:
        system = eq.include_equation(
            system,
            eq.LinearEquation(row, rhs=0)
        )
    return Matrix(system)


def apply_ero(A: Matrix, ero):
    eq.apply_ero(A.ls, ero)


def to_rref(A: Matrix):
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
                if A.sub(row, col) != 0:
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


