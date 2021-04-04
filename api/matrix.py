
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
            output += '| '
            for j in range(1, self.n + 1):
                output += '{:^5}'.format(f'{self.sub(i, j)}')
            output += '|\n'
        return output

    def copy(self):
        return Matrix(self.ls)

    def sub(self, i: int, j: int):
        row = self.ls.e[i]
        assert isinstance(row, eq.LinearEquation)
        return row.a.sub(j)


def create_matrix(grid) -> Matrix:
    system = eq.LinearSystem()
    for row in grid:
        system = eq.include_equation(
            system,
            eq.LinearEquation(row, rhs=0)
        )
    return Matrix(system)

