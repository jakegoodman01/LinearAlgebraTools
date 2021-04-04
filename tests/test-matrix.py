import unittest

from api import equation as eq
from api import vector as vc
from api import matrix as mx


class TestMatrix(unittest.TestCase):
    def test_repr(self):
        grid = [
            [1, 2, 0, 0],
            [1, 2, 3, 1],
            [-1, -1, 1, 1],
            [0, 1, 1, 1],
            [0, -1, 2, 0]
        ]
        A = mx.create_matrix(grid)
        A.augment_with(vc.Vector(1, 0, -2, -1, 0))

        mx.apply_ero(A, eq.ERO(3, [2, 1, -1]))
        mx.apply_ero(A, eq.ERO(3, [3, 1, 1]))
        mx.apply_ero(A, eq.ERO(1, [2, 3]))
        print(A)


if __name__ == '__main__':
    unittest.main()
