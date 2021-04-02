import unittest

from api import vector as vc


class TestVector(unittest.TestCase):
    def setUp(self):
        # Create some vectors
        self.v1 = vc.Vector([1, 2, 3])
        self.v2 = vc.Vector([1, 2, 3])
        self.v3 = vc.Vector([1, 2, 4])
        self.u = vc.Vector([3, -5, 7])
        self.w = vc.Vector([9, 2, -1])
        self.zero3 = self.v1.zero_vector()
        self.v1plusv3 = vc.vector_add(self.v1, self.v3)

    def test_constructor(self):
        self.assertEqual(self.v1.dim, 3)
        self.assertEqual(self.v1.components[0], 1)
        self.assertEqual(self.v1.components[1], 2)
        self.assertEqual(self.v1.components[2], 3)

    def test_zero_vector(self):
        self.assertEqual(self.zero3.dim, 3)
        for i in range(3):
            self.assertEqual(self.zero3.components[i], 0)

    def test_copy(self):
        self.assertTrue(
            vc.vector_equals(
                self.v1, self.v1.copy()
            )
        )

    def test_vector_equals(self):
        self.assertTrue(vc.vector_equals(self.v1, self.v2))
        self.assertFalse(vc.vector_equals(self.v1, self.v3))

    def test_vector_add(self):
        self.assertTrue(
            vc.vector_equals(self.v1plusv3, vc.Vector([2, 4, 7]))
        )
        self.assertTrue(
            # Asserts: u + 0 = 0 + u = u
            vc.vector_equals(
                vc.vector_add(self.zero3, self.v1),
                vc.vector_add(self.v1, self.zero3)
            )
            and
            vc.vector_equals(
                vc.vector_add(self.v1, self.zero3),
                self.v1
            )
        )
        self.assertTrue(
            # Asserts: v + u + w = v + (u + w)
            vc.vector_equals(
                vc.vector_add(self.v1, self.u, self.w),
                vc.vector_add(self.v1, vc.vector_add(self.u, self.w))
            )
        )
        self.assertTrue(
            # Asserts: v + u + w = (v + u) + w
            vc.vector_equals(
                vc.vector_add(self.v1, self.u, self.w),
                vc.vector_add(vc.vector_add(self.v1, self.u), self.w)
            )
        )
        self.assertTrue(
            # Asserts: v + u = u + v
            vc.vector_equals(
                vc.vector_add(self.v1, self.u), vc.vector_add(self.u, self.v1)
            )
        )

    def test_vector_negate(self):
        self.assertTrue(
            vc.vector_equals(
                vc.vector_negate(self.w),
                vc.Vector([-9, -2, 1])
            )
        )
        self.assertTrue(
            vc.vector_equals(self.zero3, vc.vector_negate(self.zero3))
        )
        self.assertTrue(
            vc.vector_equals(
                vc.vector_add(vc.vector_negate(self.w), self.w),
                self.zero3
            )
        )

    def test_vector_subtract(self):
        self.assertTrue(
            vc.vector_equals(
                vc.vector_subtract(self.v1, self.u),
                vc.Vector([-2, 7, -4])
            )
        )
        self.assertTrue(
            vc.vector_equals(
                vc.vector_subtract(self.w, self.w),
                self.zero3
            )
        )


if __name__ == '__main__':
    unittest.main()
