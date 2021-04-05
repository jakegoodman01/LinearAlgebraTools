
from typing import List
from api import vector as vc


class LinearEquation:
    def __init__(self, loc, rhs):
        self.n = len(loc)
        self.a = vc.Vector(*loc)
        self.rhs = rhs

    def __repr__(self):
        output = ''
        if self.a.sub(1) != 0:
            output += f'({self.a.sub(1):^.2g})y{1}'
        for i in range(2, self.n + 1):
            if self.a.sub(i) != 0:
                if output != '':
                    output += ' + '
                output += f'({self.a.sub(i):^.2g})y{i}'
        if not is_trivial_equation(self):
            output += f' = {self.rhs:^.2g}'
        return output

    def copy(self):
        return LinearEquation(self.a.components, self.rhs)


class LinearSystem:
    def __init__(self, *args: LinearEquation):
        self.m = len(args)
        self.n = 0
        for i in range(self.m):
            assert isinstance(args[i], LinearEquation)
            self.n = max(self.n, args[i].n)
        self.e = [None]
        for i in range(self.m):
            # padding shorter equations with zeros
            vc.extend_zeros(args[i].a, self.n - args[i].n)
            args[i].n = self.n
            self.e.append(args[i])

    def __repr__(self):
        output = '[\n'
        for eq in self.e[1:]:
            output += f'\t{eq.__repr__()}\n'
        return output + ']'

    def copy(self):
        equations = [eq.copy() for eq in self.e[1:]]
        return LinearSystem(*equations)


class ERO:
    def __init__(self, t: int, instr: List[int]):
        assert t == 1 or t == 2 or t == 3, f"Invalid ERO type: {t}"
        self.t = t
        self.instr = instr
        if self.t == 1:
            assert len(self.instr) == 2
        elif self.t == 2:
            assert len(self.instr) == 2
            assert self.instr[1] != 0
        else:
            assert len(self.instr) == 3
            assert self.instr[0] != self.instr[1]


def add(le1: LinearEquation, le2: LinearEquation, *args: LinearEquation) -> LinearEquation:
    system = LinearSystem(le1, le2, *args)
    coefficients = []
    for i in range(1, system.n + 1):
        coefficients.append(
            sum(eq.a.sub(i) for eq in system.e[1:])
        )
    rhs = sum(eq.rhs for eq in system.e[1:])
    eq = LinearEquation(coefficients, rhs)
    return eq


def negate(le: LinearEquation) -> LinearEquation:
    eq = le.copy()
    for i in range(le.n):
        eq.a.components[i] *= -1
    eq.rhs *= -1
    return eq


def subtract(le1: LinearEquation, le2: LinearEquation) -> LinearEquation:
    return add(le1, negate(le2))


def scalar_multiply(le: LinearEquation, s):
    for i in range(le.n):
        le.a.components[i] *= s
    le.rhs *= s


def solves_equation(le: LinearEquation, v: vc.Vector) -> bool:
    w = vc.Vector(*le.a.components)
    ans = vc.dot_product(v, w)
    return ans == le.rhs


def solves_system(ls: LinearSystem, v: vc.Vector) -> bool:
    for le in ls.e[1:]:
        if not solves_equation(le, v):
            return False
    return True


def equations_are_identical(le1: LinearEquation, le2: LinearEquation) -> bool:
    assert le1.n == le2.n, "Given equations have different number of unknowns"
    for i in range(1, le1.n + 1):
        if le1.a.sub(i) != le2.a.sub(i):
            return False
    return le1.rhs == le2.rhs


def systems_are_identical(ls1: LinearSystem, ls2: LinearSystem) -> bool:
    assert ls1.m == ls2.m, "Given systems have different number of equations"
    assert ls1.n == ls2.n, "Given systems have different number of unknowns"
    for i in range(1, ls1.m + 1):
        if not equations_are_identical(ls1.e[i], ls2.e[i]):
            return False
    return True


def apply_ero(ls: LinearSystem, ero: ERO):
    if ero.t == 1:
        i, j = ero.instr
        ls.e[i], ls.e[j] = ls.e[j], ls.e[i]
    elif ero.t == 2:
        i, k = ero.instr
        scalar_multiply(ls.e[i], k)
    else:
        i, j, c = ero.instr
        scaled = ls.e[j].copy()
        scalar_multiply(scaled, c)
        ls.e[i] = add(ls.e[i], scaled)


def include_equation(ls: LinearSystem, *args: LinearEquation) -> LinearSystem:
    for e in args:
        assert isinstance(e, LinearEquation)
    equations = ls.e[1:] + list(args)
    return LinearSystem(*equations)


def is_trivial_equation(le: LinearEquation) -> bool:
    return le.a.is_zero() and le.rhs == 0


def is_inconsistent_equation(le: LinearEquation) -> bool:
    return le.a.is_zero() and le.rhs != 0






















