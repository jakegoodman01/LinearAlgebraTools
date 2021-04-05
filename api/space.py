
import api.vector as vc
import api.matrix as mx


class Span:
    def __init__(self, *args: vc.Vector):
        assert 0 < len(args), "must have at least 1 vector in the span"
        normalized = []
        for v in args:
            normalized.append(vc.normalize(v))
        self.vectors = set(normalized)
        # TODO: Reduce the linear combinations in the span


class Line:
    def __init__(self, v: vc.Vector, w: vc.Vector):
        assert v.dim == w.dim, "v and w must be of the same dimension"
        assert v.field == w.field, "v and w must be in the same field"
        assert not w.is_zero(), "w cannot be the zero vector"
        self.v = v
        self.w = w
        self.field = v.field

    def __repr__(self):
        return '{' + f'{self.v} + t{self.w}: t e {self.field}' + '}'


class Plane:
    def __init__(self, p: vc.Vector, v: vc.Vector, w: vc.Vector):
        assert p.dim == v.dim == w.dim, "p, v and w must be of the same dimension"
        assert p.field == v.field == w.field, "p, v and w must be in the same field"
        assert not v.is_zero(), "v cannot be the zero vector"
        assert not w.is_zero(), "w cannot be the zero vector"
        assert not vc.is_scalar_multiple(w, v), "w cannot be a scalar multiple of v"
        self.p = p
        self.v = v
        self.w = w
        self.field = v.field

    def __repr__(self):
        return '{' + f'{self.p} + s{self.v} + t{self.w}: s,t e {self.field}' + '}'


def span_is_equal(S: Span, U: Span) -> bool:
    # TODO: this is currently incorrect
    if len(S.vectors) != len(U.vectors):
        return False
    for v in S.vectors:
        matched = False
        for w in U.vectors:
            if vc.is_equal(v, w):
                matched = True
                break
        if not matched:
            return False
    return True


def contained_in_span(v: vc.Vector, S: Span) -> bool:
    # TODO...
    return True


def line_passing_through(v: vc.Vector, w: vc.Vector) -> Line:
    m = vc.subtract(w, v)
    return Line(v, m)


def lies_on_line(L: Line, v: vc.Vector) -> bool:
    return vc.is_scalar_multiple(
        vc.subtract(v, L.v),
        L.w
    )


def line_is_equal(L: Line, Y: Line) -> bool:
    return lies_on_line(L, Y.v) and vc.is_scalar_multiple(L.w, Y.w)


def plane_passing_through(p: vc.Vector, r: vc.Vector, q: vc.Vector) -> Plane:
    v = vc.subtract(r, p)
    w = vc.subtract(q, p)
    return Plane(p, v, w)


def lies_on_plane(P: Plane, v: vc.Vector) -> bool:
    return contained_in_span(
        vc.subtract(v, P.p),
        Span(P.v, P.w)
    )


def plane_is_equal(P: Plane, Y: Plane) -> bool:
    return lies_on_plane(P, Y.p) and span_is_equal(
        Span(P.v, P.w),
        Span(Y.v, Y.w)
    )




































