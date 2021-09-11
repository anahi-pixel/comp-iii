import math
from typing import Callable, NamedTuple


class classproperty(property):
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


class Point(NamedTuple):
    x: float
    y: float

    def getTuple(self):
        return self.x, self.y


class FunctionApproximation:
    @staticmethod
    def sign(x: float) -> int:
        return (x > 0) - (x < 0)

    _base_epsilon = None

    @classproperty
    def floatEpsilon(cls):
        if cls._base_epsilon is None:
            eps = 1.0
            while eps + 1 > 1:
                eps /= 2
            cls._base_epsilon = eps
        return cls._base_epsilon

    # get the least measurable difference around x
    @classmethod
    def getEpsilon(cls, x: float) -> float:
        mag = math.floor(math.log2(math.fabs(x))) + 1 if x != 0 else 0
        return cls.floatEpsilon * (2 ** mag)

    @classmethod
    def isBelowThreshold(cls, x1: float, x2: float) -> bool:
        return math.fabs(x2 - x1) <= cls.getEpsilon(math.fabs(x1))

    @staticmethod
    def midpoint(x1: float, x2: float) -> float:
        return (x1 + x2)/2

    @classmethod
    def secantMethod(cls, point_a: Point, point_b: Point, point_c: Point) -> float:

        a = point_a.x
        b, fb = point_b.getTuple()
        c, fc = point_c.getTuple()
        # this shouldn't be much overhead
        m = cls.midpoint(a, b)

        p = (b - c) * fb
        p_sign = cls.sign(p)
        q = p_sign * (fc - fb)
        p = p_sign * p

        # if the numerator is less than the denominator
        # we won't ever divide by zero!
        if p <= cls.getEpsilon(q):
            return b + cls.sign(a - b) * cls.getEpsilon(b)
        elif p <= (m - b) * q:
            # secant
            return b + p/q
        else:
            # midpoint
            return m

    @classmethod
    def dekkerMethod(cls, f: Callable[[float], float], a: float, b: float) -> float:
        if cls.sign(f(a)) == cls.sign(f(b)):
            raise Exception("Expected antipodal points!")

        # b is the best zero so far
        point_b = Point(b, f(b))
        # (a, f(a)) should be antipodal to (b, f(b)) all the time
        # so that [a, b] contains the wanted root
        point_a = Point(a, f(a))
        # c is the previous value of b
        point_c = Point(a, f(a))

        while True:
            # if they're the same sign, a should be c
            if cls.sign(point_a.y) == cls.sign(point_b.y):
                point_a = point_c

            # fb should always be the smallest value
            if math.fabs(point_a.y) < math.fabs(point_b.y):
                point_c = point_b
                point_b = point_a
                point_a = point_c

            m = cls.midpoint(point_a.x, point_b.x)

            if cls.isBelowThreshold(m, point_b.x):
                break

            s = cls.secantMethod(point_a, point_b, point_c)

            # record previous point
            point_c = point_b
            # then update the best root
            point_b = Point(s, f(s))

        return point_b.x


def main(args: list[str]) -> None:
    if len(args) == 0:
        print(FunctionApproximation.dekkerMethod(lambda x: 1/(x - 3) - 6, 3.1, 3.4))
    pass


if __name__ == '__main__':
    import sys

    main(sys.argv[1:])
