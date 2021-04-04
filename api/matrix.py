
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
            output += '['
            for j in range(1, self.n + 1):
                output += '{:^5}'.format(f'{self.sub(i, j)}')
            if self.augmented:
                output += '|{:^5}'.format(f'{self.aug(i)}')
            output += ']\n'
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

