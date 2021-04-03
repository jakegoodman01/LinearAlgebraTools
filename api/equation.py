
from api import vector as vc

class LinearEquation:
    def __init__(self, loc, rhs):
        self.n = len(loc)
        self.a = [None] + loc  # offset loc by 1
        self.rhs = rhs

    def __repr__(self):
        output = ''
        output += f'{self.a[1]}*x{1}'
        for i in range(2, self.n + 1):
            output += f' + {self.a[i]}*x{i}'
        output += f' = {self.rhs}'
        return output


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
            args[i].a += [0] * (self.n - args[i].n)
            args[i].n = self.n
            assert args[i].n + 1 == len(args[i].a)
            self.e.append(args[i])

    def __repr__(self):
        output = '[\n'
        for eq in self.e[1:]:
            output += f'\t{eq.__repr__()}\n'
        return output + ']'


def solves_equation(le: LinearEquation, v: vc.Vector) -> bool:
    w = vc.Vector(*le.a[1:])
    ans = vc.dot_product(v, w)
    return ans == le.rhs


def solves_system(ls: LinearSystem, v: vc.Vector) -> bool:
    for le in ls.e[1:]:
        if not solves_equation(le, v):
            return False
    return True




























