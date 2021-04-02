import unittest

from api import vector as vc
from math import sqrt

TOLERANCE = 0.001


class TestVector(unittest.TestCase):
    def setUp(self):
        # Create some vectors
        self.v1 = vc.Vector(1, 2, 3)
        self.v2 = vc.Vector(1, 2, 3)
        self.v3 = vc.Vector(1, 2, 4)
        self.u = vc.Vector(3, -5, 7)
        self.w = vc.Vector(9, 2, -1)
        self.zero3 = self.v1.zero_vector()
        self.v1plusv3 = vc.add(self.v1, self.v3)

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
            vc.is_equal(
                self.v1, self.v1.copy()
            )
        )

    def test_equals(self):
        self.assertTrue(vc.is_equal(self.v1, self.v2))
        self.assertFalse(vc.is_equal(self.v1, self.v3))

    def test_add(self):
        self.assertTrue(
            vc.is_equal(self.v1plusv3, vc.Vector(2, 4, 7))
        )
        self.assertTrue(
            # Asserts: u + 0 = 0 + u = u
            vc.is_equal(
                vc.add(self.zero3, self.v1),
                vc.add(self.v1, self.zero3)
            )
            and
            vc.is_equal(
                vc.add(self.v1, self.zero3),
                self.v1
            )
        )
        self.assertTrue(
            # Asserts: v + u + w = v + (u + w)
            vc.is_equal(
                vc.add(self.v1, self.u, self.w),
                vc.add(self.v1, vc.add(self.u, self.w))
            )
        )
        self.assertTrue(
            # Asserts: v + u + w = (v + u) + w
            vc.is_equal(
                vc.add(self.v1, self.u, self.w),
                vc.add(vc.add(self.v1, self.u), self.w)
            )
        )
        self.assertTrue(
            # Asserts: v + u = u + v
            vc.is_equal(
                vc.add(self.v1, self.u), vc.add(self.u, self.v1)
            )
        )

    def test_negate(self):
        self.assertTrue(
            vc.is_equal(
                vc.negate(self.w),
                vc.Vector(-9, -2, 1)
            )
        )
        self.assertTrue(
            vc.is_equal(self.zero3, vc.negate(self.zero3))
        )
        self.assertTrue(
            vc.is_equal(
                vc.add(vc.negate(self.w), self.w),
                self.zero3
            )
        )

    def test_subtract(self):
        self.assertTrue(
            vc.is_equal(
                vc.subtract(self.v1, self.u),
                vc.Vector(-2, 7, -4)
            )
        )
        self.assertTrue(
            vc.is_equal(
                vc.subtract(self.w, self.w),
                self.zero3
            )
        )

    def test_scalar_multiply(self):
        p = 2
        q = -3
        self.assertTrue(
            # Asserts: (p + q)w = pw + qw
            vc.is_equal(
                vc.scalar_multiply(self.w, p + q),
                vc.add(
                    vc.scalar_multiply(self.w, p),
                    vc.scalar_multiply(self.w, q)
                )
            )
        )
        self.assertTrue(
            # Asserts: (pq)v = p(qv)
            vc.is_equal(
                vc.scalar_multiply(self.u, p * q),
                vc.scalar_multiply(
                    vc.scalar_multiply(self.u, q),
                    p
                )
            )
        )
        self.assertTrue(
            # Asserts: p(u + w) = pu + pw
            vc.is_equal(
                vc.scalar_multiply(
                    vc.add(self.u, self.w),
                    p
                ),
                vc.add(
                    vc.scalar_multiply(self.u, p),
                    vc.scalar_multiply(self.w, p)
                )
            )
        )
        self.assertTrue(
            # Asserts: 0u = 0
            vc.scalar_multiply(self.w, 0).is_zero()
        )

    def test_dot_product(self):
        a = vc.Vector(2, 3)
        b = vc.Vector(5, 7)
        self.assertEqual(vc.dot_product(a, b), 31)
        a = vc.Vector(3, -5, 2)
        b = vc.Vector(-4, 4, -2)
        self.assertEqual(vc.dot_product(a, b), -36)
        self.assertEqual(
            # Asserts: v * w = w * v
            vc.dot_product(self.u, self.w),
            vc.dot_product(self.w, self.u)
        )
        self.assertEqual(
            # Asserts: (v + u) * w = v * w + u * w (additivity)
            vc.dot_product(
                vc.add(self.v1, self.u),
                self.w
            ),
            vc.dot_product(self.v1, self.w) + vc.dot_product(self.u, self.w)
        )
        s = 3
        self.assertEqual(
            # Asserts: (sw) * u = s(w * u) (multiplicity)
            vc.dot_product(
                vc.scalar_multiply(self.w, s),
                self.u
            ),
            vc.dot_product(self.w, self.u) * s
        )

    def test_norm(self):
        a = 4
        self.assertEqual(
            # Asserts: norm(av) = |a| * norm(v)
            vc.norm(vc.scalar_multiply(self.u, a)),
            abs(a) * vc.norm(self.u)
        )
        a = vc.Vector(complex(2, -1), complex(-3, 2), complex(-4, -5))
        self.assertTrue(
            abs(vc.norm(a) - sqrt(59)) < TOLERANCE
        )
        print(a.field == 'complex')
        self.assertTrue(
            abs(vc.norm(vc.scalar_multiply(a, complex(1, 2))) - sqrt(295)) < TOLERANCE
        )

    def test_normalize(self):
        a = vc.Vector(10, 0, 0)
        self.assertTrue(
            vc.is_equal(
                vc.normalize(a),
                vc.Vector(1, 0, 0)
            )
        )

    def test_angle(self):
        a = vc.Vector(1, 4)
        b = vc.Vector(-2, 3)
        self.assertTrue(
            abs(vc.angle(a, b) - 0.833) < TOLERANCE
        )
        a = vc.Vector(1, 3, 5)
        b = vc.Vector(2, -4, 3)
        self.assertTrue(
            abs(vc.angle(a, b) - 1.413) < TOLERANCE
        )

    def test_proj(self):
        a = vc.Vector(3, -4, 5)
        b = vc.Vector(1, 2, 3)
        self.assertTrue(
            vc.is_equal(
                vc.proj(a, b),
                vc.scalar_multiply(b, 5/7)
            )
        )
        a = vc.Vector(complex(1, 0), complex(0, 1), complex(1, 1))
        b = vc.Vector(complex(1, -1), complex(2, -1), complex(3, 1))
        self.assertTrue(
            vc.is_equal(
                vc.proj(a, b),
                vc.scalar_multiply(b, complex(4, 5) / 17)
            )
        )

    def test_component(self):
        a = vc.Vector(3, -4, 5)
        b = vc.Vector(1, 2, 3)
        self.assertTrue(
            abs(vc.component(a, b) - (5 / 7) * sqrt(14)) < TOLERANCE
        )

    def test_perp(self):
        a = vc.Vector(3, -4, 5)
        b = vc.Vector(1, 2, 3)
        self.assertTrue(
            vc.is_equal(
                vc.perp(a, b),
                vc.scalar_multiply(vc.Vector(16, -38, 20), 1/7)
            )
        )

    def test_modulus(self):
        z = complex(2, -3)
        self.assertTrue(
            abs(vc.modulus(z) - sqrt(13)) < TOLERANCE
        )

    def test_inner_product(self):
        a = vc.Vector(complex(2, -3), complex(1, -2))
        b = vc.Vector(complex(-3, 4), complex(3, 5))
        self.assertEqual(vc.inner_product(a, b), complex(-25, -10))

    def test_cross_product(self):
        a = vc.Vector(2, -3, 5)
        b = vc.Vector(-2, 1, 4)
        z = vc.cross_product(a, b)
        self.assertTrue(
            vc.is_equal(z, vc.Vector(-17, -18, -4))
        )
        self.assertTrue(
            vc.is_orthogonal(a, z) and vc.is_orthogonal(b, z)
        )


if __name__ == '__main__':
    unittest.main()
