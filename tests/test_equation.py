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


if __name__ == '__main__':
    unittest.main()
