import unittest

from api import vector as vc
from api import space as sp


class TestSpaces(unittest.TestCase):
    def test_span_is_equal(self):
        s = sp.Span(vc.Vector(3, 3), vc.Vector(1, 2))
        u = sp.Span(vc.Vector(2, 4), vc.Vector(1, 1))
        self.assertTrue(
            sp.span_is_equal(s, u)
        )

    def test_line_passing_through(self):
        L = sp.line_passing_through(vc.Vector(2, -3, 5), vc.Vector(4, -2, 6))
        Y = sp.Line(vc.Vector(0, -4, 4), vc.Vector(1, 0.5, 0.5))
        self.assertTrue(sp.line_is_equal(L, Y))

    def test_lies_on_line(self):
        L = sp.Line(vc.Vector(1, 5), vc.Vector(1, 3))  # this is the line y = 2 + 3x
        self.assertTrue(sp.lies_on_line(L, vc.Vector(-1, -1)))
        self.assertFalse(sp.lies_on_line(L, vc.Vector(0, 0)))

    def test_plane_passing_through(self):
        P = sp.plane_passing_through(vc.Vector(1, 0, 0), vc.Vector(1, 1, 0), vc.Vector(1, 0, 1))
        Y = sp.plane_passing_through(vc.Vector(1, 1, 1), vc.Vector(1, 10, 2), vc.Vector(1, 0, 2))
        # self.assertTrue(sp.plane_is_equal(P, Y)) - this should be true!!!


if __name__ == '__main__':
    unittest.main()
