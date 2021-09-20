from typing import Callable, NamedTuple


class Point(NamedTuple):
    x: float
    y: float

    def getTuple(self):
        return self.x, self.y
