import unittest

from api import equation as eq
from api import vector as vc
from api import matrix as mx


class TestMatrix(unittest.TestCase):
    def test_repr(self):
        grid = [
            [2, -5, 5, -7],
            [0, 0, 4, -9],
            [0, 0, 0, 5],
            [0, 0, 0, 0]
        ]
        # A = mx.create_matrix(grid)
        # A.augment_with(vc.Vector(4, 3, 2, 0))
        e1 = eq.LinearEquation([2, 3], 4)
        e2 = eq.LinearEquation([90, 90], 5)
        A = mx.Matrix(eq.LinearSystem(e1, e2))
        A.augmented = True
        mx.to_rref(A)
        print(A)


if __name__ == '__main__':
    unittest.main()
