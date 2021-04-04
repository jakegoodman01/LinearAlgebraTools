import unittest

from api import equation as eq
from api import vector as vc
from api import matrix as mx


class TestMatrix(unittest.TestCase):
    def test_repr(self):
        grid = [
            [3, -4, -1, -19],
            [2, -3, 1, -22],
            [1, 2, -1, 7],
            [6, -12, 2, -70]
        ]
        A = mx.create_matrix(grid)
        A.augment_with(vc.Vector(-8, -1, 2, -12))
        print(A.ls)
        mx.to_rref(A)
        print(A.ls)


if __name__ == '__main__':
    unittest.main()
