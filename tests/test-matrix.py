import unittest

from api import equation as eq
from api import vector as vc
from api import matrix as mx


class TestMatrix(unittest.TestCase):
    def test_repr(self):
        A = mx.create_matrix([
            [1, 1],
            [0, 0]
        ])
        B = mx.create_matrix([
            [1, 2],
            [3, 4]
        ])
        print(mx.matrix_matrix_product(A, B))
        print(mx.matrix_matrix_product(B, A))

    def test_sub(self):
        grid = [
            [1, 2],
            [-3, -4],
            [7, 9]
        ]
        A = mx.create_matrix(grid)
        self.assertEqual(A.sub(1, 2), 2)
        self.assertEqual(A.sub(2, 2), -4)
        self.assertEqual(A.sub(3, 1), 7)
        #print(A.row(1))

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

    def test_super_matrix(self):
        a_grid = [
            [1, -2, -1, 3],
            [2, -4, 1, 0],
            [1, -2, 2, -3]
        ]
        b_grid = [
            [1, 1, -1, 0],
            [5, 2, 4, 0],
            [4, 3, 5, 0]
        ]
        sam = mx.SuperAugmentedMatrix(
            mx.create_matrix(a_grid),
            mx.create_matrix(b_grid)
        )
        mx.to_rref(sam)
        # print(sam)

    def test_complex_example(self):
        grid = [
            [complex(1, 1), complex(-2, -3)],
            [complex(4, 5), complex(3, -2)]
        ]
        b = vc.Vector(complex(0, -15), complex(37, -7))
        A = mx.create_matrix(grid)
        A.augment_with(b)
        mx.to_rref(A)
        # print(A)

    def test_matrix_vector_product(self):
        A = mx.create_matrix([
            [1, 6, 1],
            [3, 4, 5],
            [5, 2, -3]
        ])
        x = vc.Vector(1, -4, 6)
        prod = mx.matrix_vector_product(A, x)
        self.assertTrue(
            vc.is_equal(
                prod,
                vc.Vector(-17, 17, -21)
            )
        )
        A = mx.create_matrix([
            [complex(1, 1), complex(2, 2), complex(3, -1)],
            [complex(2, 3), complex(4, 1), complex(5, -2)]
        ])
        x = vc.Vector(1, complex(1, -1), complex(2, -3))
        prod = mx.matrix_vector_product(A, x)
        self.assertTrue(
            vc.is_equal(
                prod,
                vc.Vector(complex(8, -10), complex(11, -19))
            )
        )

    def test_matrix_matrix_product(self):
        # Test 1
        A = mx.create_matrix([
            [1, 2],
            [3, 5],
            [8, 7]
        ])
        B = mx.create_matrix([
            [-1, 3],
            [2, -4]
        ])
        ans = mx.create_matrix([
            [3, -5],
            [7, -11],
            [6, -4]
        ])
        C = mx.matrix_matrix_product(A, B)
        self.assertTrue(mx.matrix_equal(C, ans))
        # Test 2
        A = mx.create_matrix([
            [complex(2, -1), complex(1, -2)],
            [complex(3, -2), complex(1, -3)]
        ])
        B = mx.create_matrix([
            [complex(1, 1), complex(-2, 1)],
            [complex(-1, 1), complex(3, 2)]
        ])
        ans = mx.create_matrix([
            [complex(4, 4), 4],
            [complex(7, 5), 5]
        ])
        C = mx.matrix_matrix_product(A, B)
        self.assertTrue(mx.matrix_equal(C, ans))


    def test_has_solution(self):
        # print(mx.identity(10))
        pass


if __name__ == '__main__':
    unittest.main()
