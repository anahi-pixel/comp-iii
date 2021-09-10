import math
from typing import Callable

from functions.function_meta import ContinuousFunction, ContinuousFunctionMeta
from point import Point


def testFunction(mass: float, gravity: float) -> Callable[[float], float]:
    def f(x: float) -> float:
        return gravity*x**2 - mass*math.exp(x)

    return f

TEST_FUNCTION = ContinuousFunction(
    ContinuousFunctionMeta(
        "Test function",
        "Function used for testing under normal conditions"
    ),
    testFunction
)
