import math
from typing import Callable


sign = lambda a: (a > 0) - (a < 0)


class FunctionApproximation:

    def __init__(self, f: Callable[[float], float], a0: float, b0: float) -> None:

        if sign(f(a0)) == sign(f(b0)):
            raise Exception("Expected antipodal points!")

        self.f = f
        self.a = a0
        self.b = b0
        eps = 1.0
        while eps + 1 > 1:
            eps /= 2
        self._base_eps = eps

    # get the least measurable difference around x
    def getEpsilon(self, x: float) -> float:
        mag = math.floor(math.log2(math.fabs(x))) + 1
        return self._base_eps * (2 ** mag)

    def isBelowThreshold(self, x1: float, x2: float) -> bool:
        return math.fabs(x2 - x1) <= self.getEpsilon(math.fabs(x1))

    def secantLine(self, x1: float, x2: float) -> Callable[[float], float]:
        return (f(x2) - f(x1))/(x2 - x1)

    def secantMethod(self, a: float, b: float, c: float) -> float:
        # (f(x_k) - f(x_n))/(x_k+1 - x_k) = (f(x2) - f(x1))/(x2 - x1)
        #secant = self.secantLine(x1, x2)

        #if secant == 0:
        #    return bisectionMethod(x1, x2)

        #return x2 - (1/secant) * self.f(x2)

        m = self.bisectionMethod(a, b)

        p = (b - c) * self.f(b)
        if p >= 0:
            q = self.f(c) - self.f(b)
        else:
            q = self.f(b) - self.f(c)
            p = -p

        # if the numerator is less than the denominator
        # we won't ever divide by zero!
        if p <= self.getEpsilon(q):
            return b + sign(a - b) * self.getEpsilon(b)
        elif p <= (m - b) * q:
            # secant
            return b + p/q
        else:
            return m

    def bisectionMethod(self, x1: float, x2: float) -> float:
        return (x1 + x2)/2

    def dekkerMethod(self, a: float = None, b: float = None) -> float:
        # b is the best zero so far
        b = b if b is not None else self.b
        fb = self.f(b)
        # (a,fa) should be antipodal to (b,fb) all the time
        # so that [a, b] contains the wanted root
        a = a if a is not None else self.a
        fa = self.f(a)
        # c is the previous value of b
        c = a
        fc = fa

        while True:
            # if they're the same sign, a should be c
            if sign(fa) == sign(fb):
                a = c
                fa = fc

            # fb should always be the smallest value
            if math.fabs(fa) < math.fabs(fb):
                c, b, a = b, a, c
                fc, fb, fa = fb, fa, fc

            m = self.bisectionMethod(a, b)

            if self.isBelowThreshold(m, b):
                break

            s = self.secantMethod(a, b, c)

            # record previous point
            c = b
            fc = fb
            # then update the best root
            b = s
            fb = self.f(b)

        return b


def main(args: list[str]) -> None:
    if len(args) == 0:
        approx = FunctionApproximation(lambda x: 1/(x - 3) - 6, 3.1, 3.4)
        print(approx.dekkerMethod())
    pass


if __name__ == '__main__':
    import sys

    main(sys.argv[1:])
