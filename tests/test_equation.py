import unittest

from api import equation as eq
from api import vector as vc


class TestLinearSystem(unittest.TestCase):
    def test_solves_system(self):
        e1 = eq.LinearEquation([1, -2, 3], 1)
        e2 = eq.LinearEquation([2, -4, 6], 2)
        e3 = eq.LinearEquation([3, -1, 1], 3)
        system = eq.LinearSystem(e1, e2, e3)
        self.assertTrue(eq.solves_system(system, vc.Vector(1, 0, 0)))
        self.assertFalse(eq.solves_system(system, vc.Vector(-2, 0, 1)))

    def test_add(self):
        e1 = eq.LinearEquation([-2, -4, -6], 4)
        e2 = eq.LinearEquation([3, 6, 10], 6)
        e3 = eq.LinearEquation([0, 1, 2], 5)
        le = eq.LinearEquation([1, 3, 6], 15)
        self.assertTrue(
            eq.equations_are_identical(
                eq.add(e1, e2, e3),
                le
            )
        )

    def test_apply_ero(self):
        e1 = eq.LinearEquation([-2, -4, -6], 4)
        e2 = eq.LinearEquation([3, 6, 10], 6)
        e3 = eq.LinearEquation([0, 1, 2], 5)
        ls = eq.LinearSystem(e1, e2, e3)

        ero = eq.ERO(2, [1, -0.5])
        eq.apply_ero(ls, ero)
        ero = eq.ERO(3, [2, 1, -3])
        eq.apply_ero(ls, ero)
        ero = eq.ERO(1, [2, 3])
        eq.apply_ero(ls, ero)
        ero = eq.ERO(3, [2, 3, -2])
        eq.apply_ero(ls, ero)
        ero = eq.ERO(3, [1, 3, -3])
        eq.apply_ero(ls, ero)
        ero = eq.ERO(3, [1, 2, -2])
        eq.apply_ero(ls, ero)

        self.assertTrue(
            eq.systems_are_identical(
                ls,
                eq.LinearSystem(
                    eq.LinearEquation([1, 0, 0], 0),
                    eq.LinearEquation([0, 1, 0], -19),
                    eq.LinearEquation([0, 0, 1], 12)
                )
            )
        )

    def test_include_equation(self):
        e1 = eq.LinearEquation([1, -2, 3], 1)
        e2 = eq.LinearEquation([2, -4, 6], 2)
        e3 = eq.LinearEquation([3, -1, 1], 3)

        ls = eq.LinearSystem()
        ls = eq.include_equation(ls, e1)
        ls = eq.include_equation(ls, e2, e3)
        self.assertTrue(eq.systems_are_identical(ls, eq.LinearSystem(e1, e2, e3)))


if __name__ == '__main__':
    unittest.main()
