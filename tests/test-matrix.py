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
        A = mx.create_matrix(grid)
        A.augment_with(vc.Vector(4, 3, 2, 0))
        print(mx.homogeneous(A))

    def test_rref(self):
        grid = [
            [1, -2, -1, 3],
            [2, -4, 1, 0],
            [1, -2, 2, -3]
        ]
        A = mx.create_matrix(grid)
        A.augment_with(vc.Vector(1, 5, 4))
        mx.to_rref(A)
        self.assertTrue(mx.is_consistent(A))

        A = mx.create_matrix(grid)
        A.augment_with(vc.Vector(1, 2, 3))
        mx.to_rref(A)
        self.assertFalse(mx.is_consistent(A))


if __name__ == '__main__':
    unittest.main()
